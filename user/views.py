from rest_framework import viewsets, permissions, serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .serializers import UserSerializer, UserRegisterSerializer, UserLoginSerializer

from rest_framework_jwt.utils import jwt_response_payload_handler, jwt_encode_handler
from rest_framework.decorators import action

from utils.response import Response


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]

    @action(methods=['GET'], detail=False, permission_classes=[permissions.IsAuthenticated])
    def profile(self, request):
        return Response.ok(self.get_serializer(request.user).data)

    @action(methods=['POST'], detail=False, permission_classes=[permissions.AllowAny],
            serializer_class=UserRegisterSerializer)
    def register(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response.ok(serializer.data)

    @action(methods=['POST'], detail=False, permission_classes=[permissions.AllowAny],
            serializer_class=UserLoginSerializer)
    def login(self, request):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token = jwt_encode_handler({'username': user.username})
        data = jwt_response_payload_handler(token, user=user)
        return Response.ok(data)
