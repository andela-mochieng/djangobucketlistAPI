"""Defines our API custom permissions"""
from rest_framework import permissions

class IsOwner(permissions.BasePermission):
    """ Grant users permission to create,read, update and delete data"""
    def has_object_permission(self,request, view, obj):
        return obj.created_by == request.user