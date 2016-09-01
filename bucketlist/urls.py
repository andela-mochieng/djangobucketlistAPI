"""Bucketlist URL Configuration
"""
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/v.1/', include('api.urls'), name='bucketlist-api'),
    url(r'^api-docs/', include('rest_framework_swagger.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
#     url('', include('social.apps.django_app.urls', namespace='social')),
]
