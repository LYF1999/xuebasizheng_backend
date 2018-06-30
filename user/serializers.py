#  coding=utf-8
from rest_framework import serializers, exceptions
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'is_staff', 'is_superuser')


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        return User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def create(self, validated_data):
        raise BaseException('can\'t create')

    def update(self, instance, validated_data):
        raise BaseException('cant\'t update')

    def validate(self, attrs):
        user = authenticate(**attrs)
        if not user:
            return exceptions.AuthenticationFailed()
        return {
            'user': user,
        }
