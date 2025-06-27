from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from drf_spectacular.utils import extend_schema
from .serializers import UserCreationSerializer, UserLoginSerializer, ProfileSerializer

# Create your views here.
class UserRegistrationView(CreateAPIView):
    serializer_class = UserCreationSerializer

@extend_schema(request=UserLoginSerializer)
class LoginView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(**serializer.validated_data)
        if user == None:
            raise serializers.ValidationError("Credentials does not match!")
        access_token = RefreshToken.for_user(user)
        token = {
            "refresh": str(access_token),
            "access": str(access_token.access_token)
        }
        return Response(token, status=status.HTTP_200_OK)


class ProfileView(RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user