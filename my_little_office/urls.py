"""my_little_office URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.utils.translation import gettext_lazy as _
from django.conf import settings

from drf_spectacular.views import (
    SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
)

admin.site.site_header = _('My Little Office Administration')

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='admin:index'), name='index'),
    path('admin/', admin.site.urls),
    path('api/', include('my_little_office.api_router')),
    path('api/schema/', include([
        path('', SpectacularAPIView.as_view(), name='schema'),
        path('swagger-ui/', SpectacularSwaggerView.as_view(),
             name='swagger-ui'),
        path('redoc/', SpectacularRedocView.as_view(), name='redoc'),
    ]))
]

if "debug_toolbar" in settings.INSTALLED_APPS:
    import debug_toolbar
    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
