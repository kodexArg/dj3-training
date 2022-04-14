"""Main URLs module."""

from socket import IP_DROP_MEMBERSHIP
from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from django.contrib import admin


urlpatterns = [
    # Django Admin
    path(settings.ADMIN_URL, admin.site.urls),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
