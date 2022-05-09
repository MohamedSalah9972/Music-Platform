from django.contrib.auth import authenticate
from django.db import models
from django.db.models import fields
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
        fields = ('id', 'username', 'email', 'password1', 'password2')

    def validate(self, attrs):
        password1 = attrs.pop('password1', '')
        password2 = attrs.pop('password2', '')
        if password1 and password2 and password1 != password2:
            raise ValidationError('password mismatch')


    def create(self, validated_data):
        password = validated_data.pop('password1', '')
        user = CustomUser.objects.create_user(**validated_data)
        user.set_password(password)
        user.save()
        return user


class RegisterSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(max_length=128, write_only=True)
    password2 = serializers.CharField(max_length=128, write_only=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')

    def create(self, validated_data):
        user = CustomUser.objects.create_user(validated_data['username'], validated_data['email'],
                                              validated_data['password1'])
        return user
