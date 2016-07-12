from django.conf.urls import url, include
from rest_framework_jwt.views import (
    obtain_jwt_token,
    refresh_jwt_token,
    verify_jwt_token,
)

from .views import *

urlpatterns = [
    url(r'^register/$', UserListView.as_view(), name='register'),
    url(r'^api-token-auth/$', obtain_jwt_token),
    url(r'^auth/token/refresh/', refresh_jwt_token),
    url(r'^auth/verify-token/', verify_jwt_token),
    url(r'^bucketlists/$', BListsView.as_view(), name='blists'),
    url(r'^bucketlists/(?P<pk>\d+)/$', SingleBListDetailView.as_view(), name='blist'),
    url(r'^bucketlists/(?P<id>\d+)/items/$', BListItemCreateView.as_view(), name='blitems'),
    url(r'^bucketlists/(?P<id>\d+)/items/(?P<pk>\d+)/$', SingleBListItem.as_view(), name='blitem'),
]


