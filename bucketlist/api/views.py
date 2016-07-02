from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import status, permissions
# from rest_framework_jwt.authentication import
from django.shortcuts import get_object_or_404
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    CreateAPIView,
)
# Create your views here.
