from django.contrib.auth.models import User
from rest_framework import serializers
from .models import BucketList, BucketListItem
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from rest_framework.serializers import (
    ModelSerializer,
)


class UserSerializer(ModelSerializer):
    password = serializers.CharField(max_length=100,
                                     style={'input_type': 'password'},
                                     required=True, write_only=True)


    def validate(self, data):
        try:
            validate_email(data['email'])
            return data
        except ValidationError:
            raise serializers.ValidationError('The email is invalid.')

    def create(self,validate_data):
        user = User.objects.create(username=validate_data['username'], email=validate_data['email'])
        user.set_password(validate_data['password'])
        user.save()
        return user


    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class BucketlistItemSerializer(ModelSerializer):
    item_name = serializers.CharField(max_length=100)
    item_description = serializers.CharField(max_length=100)

    def validate(self, data):
        """Ensure item_name is not empty."""

        if data['item_name'] == '':
            raise serializers.ValidationError('Item name can not be empty.')
        return data

    class Meta:
        model = BucketListItem
        fields = ('id', 'item_name', 'item_description', 'done', 'date_created', 'date_modified')


class BucketlistSerializer(ModelSerializer):
    # items = BucketlistItemSerializer(many=True, read_only=True)
    bucketlistitem = serializers.StringRelatedField(many=True)
    list_name = serializers.CharField(max_length=100)

    def validate(self, data):
        """Ensure list_name is not equal."""
        if data['list_name'] == '':
            raise serializers.ValidationError('List name can not be empty.')
        return data

    class Meta:
        model = BucketList
        fields = ('id', 'list_name', 'bucketlistitem', 'date_created', 'date_modified','creator')