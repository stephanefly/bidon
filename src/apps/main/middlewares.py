import time
import logging

from django.utils.deprecation import MiddlewareMixin
from django.conf import settings
from django.shortcuts import redirect

logger = logging.getLogger(__name__)

# URLs exemptées d'authentification
EXEMPT_URLS = [settings.LOGIN_URL.lstrip("/")]
if hasattr(settings, "LOGIN_EXEMPT_URLS"):
    EXEMPT_URLS += [url.lstrip("/") for url in settings.LOGIN_EXEMPT_URLS]


class TimerMiddleware(MiddlewareMixin):
    def process_request(self, request):
        request.start_time = time.time()

    def process_response(self, request, response):
        if hasattr(request, 'start_time'):
            execution_time = time.time() - request.start_time
            # logger.debug(f"Execution time: {execution_time:.3f}s")
        return response

#
# class LoginRequiredMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response
#
#     def __call__(self, request):
#         return self.get_response(request)
#
#     def process_view(self, request, view_func, view_args, view_kwargs):
#         path = request.path_info.lstrip("/")
#
#         # Ne pas rediriger si l’URL commence par une exemptée
#         if not request.user.is_authenticated and not any(path.startswith(url) for url in EXEMPT_URLS):
#             logger.info(f"User not authenticated, redirected from: {path}")
#             return redirect(f"{settings.LOGIN_URL}?next=/{path}")
#         return None
