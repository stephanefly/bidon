from .base_urls import urlpatterns as base_urlpatterns
from .perfo_0d_urls import urlpatterns as perfo_0d_urlpatterns
from .revue_veine_urls import urlpatterns as revue_veine_urlpatterns
from .revue_aube_urls import urlpatterns as revue_aube_urlpatterns
from .shenron_urls import urlpatterns as shenron_urlspatterns
from .y_to_yplus_urls import urlpatterns as y_to_yplus_urlpatterns

urlpatterns = base_urlpatterns + perfo_0d_urlpatterns + revue_veine_urlpatterns + y_to_yplus_urlpatterns + revue_aube_urlpatterns + shenron_urlspatterns
