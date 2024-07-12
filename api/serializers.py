
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Administrador, Inspector, Analista, Cliente

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class CreateUserSerializer(serializers.ModelSerializer):
    role = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'role']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        role = validated_data.pop('role')
        user = User.objects.create_user(**validated_data)
        
        if role == 'Administrador':
            Administrador.objects.create(usuario=user)
        elif role == 'Inspector':
            Inspector.objects.create(usuario=user)
        elif role == 'Analista':
            Analista.objects.create(usuario=user)
        elif role == 'Cliente':
            Cliente.objects.create(usuario=user)
        
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        from django.contrib.auth import authenticate

        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")
