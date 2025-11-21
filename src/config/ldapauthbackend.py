import json
import logging

import ldap3
from django.conf import settings
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import User
from ldap3.core.exceptions import (
    LDAPBindError,
    LDAPInvalidCredentialsResult,
    LDAPSocketOpenError,
)

logger = logging.getLogger(__name__)


class MultipleLdapUserFoundError(Exception):
    pass


class LdapAuthBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        """
        Check if the user exists in the AD.
        Get or create the returned ldap user
        """

        try:
            user_ldap = self.get_ldap3_info(username, password)
        except (LDAPSocketOpenError, LDAPBindError):
            logger.exception("Can't authenticate %s. LDAP error.", username)
            return None
        except LDAPInvalidCredentialsResult:
            logger.warning("Invalid credentials for %s", username)
            return None
        except MultipleLdapUserFoundError:
            logger.warning("Multiple users in ldap found for %s", username)
            return None

        if user_ldap is not None:
            if self.is_not_allowed_to_logon(user_ldap["memberOf"]):
                logger.warning("%s is not allow due to his groups", username)
                return None

            try:
                user = User.objects.get(username=username.lower())
            except User.DoesNotExist:
                user = User.objects.create_user(
                    username=username.lower(),
                    first_name=user_ldap["givenName"],
                    last_name=user_ldap["sn"],
                    email=user_ldap["mail"],
                )
            return user
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

    def get_ldap3_info(self, user=None, password=None):
        connection = ldap3.Connection(
            ldap3.Server(settings.LDAP_HOST, port="", use_ssl=True),
            auto_bind=ldap3.AUTO_BIND_NO_TLS,
            read_only=True,
            check_names=True,
            user=f"{settings.LDAP_DOMAIN}\\{user}",
            password=password,
        )

        connection.search(
            search_base="DC=snm,DC=snecma",
            search_filter="(&(samAccountName=" + user + "))",
            search_scope=ldap3.SUBTREE,
            attributes=ldap3.ALL_ATTRIBUTES,
            get_operational_attributes=True,
        )

        if not connection.entries:
            return None

        if len(connection.entries) > 1:
            raise MultipleLdapUserFoundError

        entries = json.loads(connection.response_to_json())["entries"][0]

        return entries["attributes"]

    def is_not_allowed_to_logon(self, user_groups):
        """
        Not allowed if the group of allowed users not in the user groups
        :return:
        """
        found_groups = [
            group_name
            for group_name in user_groups
            if settings.GROUP_OF_ALLOWED_USERS in group_name
        ]

        return not found_groups
