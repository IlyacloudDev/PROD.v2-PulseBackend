from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView, UpdateAPIView
from .models import CustomUser
from .serializers import UserRegistrationSerializer, UserProfileSerializer, UserUpdatePasswordSerializer


class PingAPIView(APIView):
    """
    Checks if the server is ready to handle requests.
    """
    def get(self, request):
        return Response("ok", status=status.HTTP_200_OK)


class UserRegisterAPIView(CreateAPIView):
    """
    Handles user registration by creating a new CustomUser instance.
    """
    queryset = CustomUser.objects.all()
    serializer_class = UserRegistrationSerializer


class UserProfileAPIView(RetrieveUpdateAPIView):
    """
    Allows the authenticated user to retrieve or update their own profile.
    """
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        """
        Override to return the currently authenticated user.
        """
        return self.request.user


class UserUpdatePasswordAPIView(UpdateAPIView):
    """
    Handles password updates for the authenticated user.
    """
    serializer_class = UserUpdatePasswordSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        """
        Override to return the currently authenticated user.
        """
        return self.request.user

    def partial_update(self, request, *args, **kwargs):
        """
        Override partial_update to modify the success response.
        """
        response = super().partial_update(request, *args, **kwargs)

        if response.status_code == 200:
            return Response({"status": "ok"}, status=response.status_code)

        return response
