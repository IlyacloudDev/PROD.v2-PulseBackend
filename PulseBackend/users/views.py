from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.generics import CreateAPIView
from .models import CustomUser
from .serializers import UserRegistrationSerializer


class PingAPIView(APIView):
    """Checks if the server is ready to handle requests."""
    def get(self, request):
        return Response("ok", status=status.HTTP_200_OK)


class UserRegisterAPIView(CreateAPIView):
    """
    Handles user registration by creating a new CustomUser instance.
    """
    queryset = CustomUser.objects.all()
    serializer_class = UserRegistrationSerializer
