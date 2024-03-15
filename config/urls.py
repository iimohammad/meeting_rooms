from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from config import settings
# from config.local_settings import *
from config.Sample_local_settings import *

urlpatterns = [
    path(Admin, admin.site.urls),  # For security Reasons, admin url can change
    path('auth/', include('accounts.urls')),
    path("__debug__/", include("debug_toolbar.urls")),
    path('company/', include('company.urls')),
    path('rooms/', include('rooms.urls')),
    path('notification/', include('notification.urls')),
    path('', include('home.urls'))
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
