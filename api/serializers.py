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
    confirm_password = serializers.CharField(max_length=100,
                                             style={'input_type': 'password'},
                                             required=True, write_only=True)

    def create(self, validated_data):
        validated_data.pop('confirm_password')
        return User.objects.create_user(**validated_data)

    def validate_email(self, email):
        existing = User.objects.filter(email=email).first()
        if existing:
            raise serializers.ValidationError("Someone with that email "
                                              "address has already registered. Was it you?")

        return email

    def validate(self, data):
        if data['password']:
            if data['password'] != data['confirm_password']:
                raise serializers.ValidationError(
                    "The passwords have to be similar"
                )
        return data

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'confirm_password')
        read_only_fields = ('id', 'confirm_password')


class LoginSerializer(ModelSerializer):
    password = serializers.CharField(
        style={'input_type': 'password'}, max_length=100, write_only=True, required=True)
    email = serializers.EmailField(
        max_length=100, required=True, write_only=True)

    class Meta:
        model = User
        fields = ('id', 'email', 'password')


class BucketlistItemSerializer(ModelSerializer):
    item_name = serializers.CharField(max_length=100)

    def validate(self, data):
        """Ensure item_name is not empty."""

        if data['item_name'] == '':
            raise serializers.ValidationError('Item name can not be empty.')
        return data

    class Meta:
        model = BucketListItem
        fields = ('id', 'item_name',
                  'done', 'date_created', 'date_modified')


class BucketlistSerializer(ModelSerializer):
    items = BucketlistItemSerializer(many=True, read_only=True)
    list_name = serializers.CharField(max_length=100)
    creator = serializers.ReadOnlyField(source='creator.id')

    def validate(self, data):
        """Ensure list_name is not equal."""
        if data['list_name'] == '':
            raise serializers.ValidationError('List name can not be empty.')
        return data

    class Meta:
        model = BucketList
        fields = ('id', 'list_name', 'creator',
                  'date_created', 'date_modified', 'items')
        read_only_fields = ('creator',)
