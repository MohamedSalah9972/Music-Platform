from abc import ABC

from django.contrib.auth import authenticate
from django.db import models
from django.db.models import fields
from knox.models import AuthToken
from rest_framework import serializers
from rest_framework.serializers import ValidationError
from users.models import CustomUser
import django.contrib.auth.password_validation as validators
from django.core import exceptions


class CustomUserSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(max_length=128, write_only=True)
    password2 = serializers.CharField(max_length=128, write_only=True)

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'password1', 'password2', 'bio')

    def validate(self, attrs):
        password1 = attrs.pop('password1', '')
        password2 = attrs.pop('password2', '')
        if password1 and password2 and password1 != password2:
            raise ValidationError('password mismatch')
        return attrs


class RegisterSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(max_length=128, write_only=True)
    password2 = serializers.CharField(max_length=128, write_only=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2', 'bio')

    def create(self, validated_data):
        user = CustomUser.objects.create_user(username=validated_data['username'], email=validated_data['email'],
                                              password=validated_data['password1'], bio=validated_data['bio'])
        return user


class LoginUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Invalid credentials.")
