from rest_framework import generics, status, permissions
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import UserSerializer, CreateUserSerializer, LoginSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from .models import Administrador, Inspector, Analista, Cliente
from rest_framework_simplejwt.exceptions import InvalidToken


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.IsAdminUser]
    serializer_class = CreateUserSerializer

class LoginView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        refresh = RefreshToken.for_user(user)
        role = None

        if Administrador.objects.filter(usuario=user).exists():
            role = 'Administrador'
        elif Inspector.objects.filter(usuario=user).exists():
            role = 'Inspector'
        elif Analista.objects.filter(usuario=user).exists():
            role = 'Analista'
        elif Cliente.objects.filter(usuario=user).exists():
            role = 'Cliente'

        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'role': role,
        }, status=status.HTTP_200_OK)

class LogoutView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
class RefreshTokenView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            new_access_token = token.access_token

            return Response({
                'access': str(new_access_token),
            }, status=status.HTTP_200_OK)
        except InvalidToken:
            return Response({
                'detail': 'Invalid token.'
            }, status=status.HTTP_400_BAD_REQUEST)