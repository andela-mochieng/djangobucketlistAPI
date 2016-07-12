from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework import filters
from rest_framework.response import Response
from .serializers import UserSerializer, BucketlistSerializer, BucketlistItemSerializer
from django.shortcuts import get_object_or_404
from rest_framework.generics import (
    CreateAPIView,
    ListCreateAPIView,  # read-write methods: GET, POST
    # read-write-update-delete methods: GET, POST,PUT, DELETE
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
)
from .permissions import IsOwnerOrReadOnly
from .models import BucketList, BucketListItem

def get_user_bucketlist(obj):
    bucketlist_id = obj.kwargs.get('id',0)
    return get_object_or_404(
        BucketList, id=int(bucketlist_id), creator=obj.request.user)
class UserListView(CreateAPIView):
    """
    Class that queries the user model, and map the user object with it's serializers
    We access backend filters
    permission_classes = [AllowAny] to allow others to access this url
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)



# Create your views here.
def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'user': user.username
    }


class BListsView(ListCreateAPIView):
    """
    Method GET: Return bucketlist
     Parameters: default page 1
     Header: Access token is required
     Response: JSON
    Method POST: Creates a new bucketlist
     Parameters: (required) list_name
     Header: Access token is required
     Response: JSON

    """
    permission_classes = (IsOwnerOrReadOnly, IsAuthenticated,)
    queryset = BucketList.objects.all()
    serializer_class = BucketlistSerializer


    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)



    def get_queryset(self):
        """Specifies the queryset used for serialization"""
        search = self.request.GET.get('s', None)
        if search:
            return BucketList.search(search)
        return BucketList.objects.all().filter(creator=self.request.user)



class SingleBListDetailView(RetrieveUpdateDestroyAPIView):
    """
    Method GET: Return single bucketlist
    Method PUT: Updates single bucketlist
    Method DELETE: deletes a single bucketlist
    They all take the following parameters
    Header:
          AccessToken  (required)
      Response: JSON
    """
    queryset = BucketList.objects.all()
    serializer_class = BucketlistSerializer
    permission_classes = (IsOwnerOrReadOnly, IsAuthenticated,)


class BListItemCreateView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = BucketlistItemSerializer
    queryset = BucketListItem.objects.all()


    def perform_create(self, serializer):
        """"""
        value = [(k, int(v)) for k, v in self.kwargs.items()]
        pk = value[0][1]
        bucketlist = get_object_or_404(
            BucketList,
            pk=pk)
        serializer.save(bucketlist=bucketlist)


class SingleBListItem(RetrieveUpdateDestroyAPIView):
    """
    Method GET- returns a single BLItem
    Method DElETE- allows users to delete a BLitem
    Header:
          AccessToken  (required)
      Response: JSON
    Method PUT - allows user to update a BLitem
    Parameters:
          item_name (optional)
          item_description (optional)
          done  (optional)
      Header:
          AccessToken  (required)
      Response: JSON
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = BucketlistItemSerializer
    queryset = BucketListItem.objects.all()



    def get_object(self):
        """
        Specify the object to be  updated,
         retrieved or delete actions
         """
        queryset = BucketListItem.objects.filter(bucketlist__creator=self.request.user, pk=self.kwargs.get('pk'))
        if queryset:
            return queryset[0]
        else:
            return "No search item create by you"

