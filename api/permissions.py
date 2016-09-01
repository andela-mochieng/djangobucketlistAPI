"""Defines our API custom permissions"""
from rest_framework.permissions import BasePermission
from .models import BucketListItem, BucketList



class IsOwnerOrReadOnly(BasePermission):
    """
    Object-level permission class to allow only an Owner to edit their bucketlist else read only"""

    def has_object_permission(self, request, view, obj):
        if type(obj) is BucketListItem:
            return obj.bucketlist.creator == request.user
        return obj.creator == request.user
