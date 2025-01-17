from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.generics import (
    CreateAPIView,
    RetrieveUpdateAPIView,
    UpdateAPIView,
    RetrieveAPIView, ListAPIView
)
from .permissions import IsProfileAccessiblePermission
from .serializers import (
    UserRegistrationSerializer,
    UserProfileSerializer,
    UserUpdatePasswordSerializer,
    UserFriendAddRemoveSerializer,
)
from .services.users_views_services import _get_users, _get_friends_of_user
from .paginations import FriendsListPagination


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


class UserDetailByLoginAPIView(RetrieveAPIView):
    """
    Retrieves the profile of a user by their login, checking access permissions.
    """
    queryset = _get_users()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated, IsProfileAccessiblePermission,]
    lookup_field = "login"


class BaseUserFriendAPIView(CreateAPIView):
    """
    Managing user friends.
    """
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        """
        Handle the friend action (add or remove).
        """
        response = super().create(request, *args, **kwargs)

        if response.status_code == 201:
            return Response({"status": "ok"})

        return response

    def get_serializer_context(self):
        """
        Add 'action' to the serializer context.
        """
        context = super().get_serializer_context()
        context['action'] = self.action
        return context


class UserFriendAddAPIView(BaseUserFriendAPIView):
    """
    Handle adding a user to the friends list.
    """
    serializer_class = UserFriendAddRemoveSerializer
    action = 'add'


class UserFriendRemoveAPIView(BaseUserFriendAPIView):
    """
    Handle removing a user from the friends list.
    """
    serializer_class = UserFriendAddRemoveSerializer
    action = 'remove'


class UserFriendsListAPIView(ListAPIView):
    """
    Handle listing the friends of the authenticated user.
    """
    serializer_class = UserFriendAddRemoveSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = FriendsListPagination

    def get_queryset(self):
        """
        Retrieve the queryset of the authenticated user's friends.
        """
        return _get_friends_of_user(self.request.user.id)

