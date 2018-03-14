"""team-up URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.decorators import user_passes_test
from django.views.generic import RedirectView
from django.views.static import serve
from rest_framework_swagger.views import get_swagger_view

from common.permissions import is_admin

from chatter.urls import urlpatterns as chatter_urlpatterns

schema_view = user_passes_test(is_admin)(get_swagger_view(title='VeeU API'))

api_urlpatterns = [
    url(r'^games/', include('games.urls', namespace='games')),
    url(r'^userprofiles/', include('userprofiles.urls', namespace='userprofiles')),
] + chatter_urlpatterns

urlpatterns = [
    url(r'^$', RedirectView.as_view(pattern_name='documentation', permanent=False)),
    url(r'^docs/$', schema_view, name='documentation'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^jet/', include('jet.urls', 'jet')),  # Django JET URLS
    url(r'^admin/', admin.site.urls),
    url(r'^auth/', include('rest_framework_social_oauth2.urls')),
    url(r'^api/', include((api_urlpatterns, 'api'), namespace='api')),
    url(r'^health/', include('health_check.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]
