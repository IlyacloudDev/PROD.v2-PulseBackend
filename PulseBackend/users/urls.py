from tkinter.font import names

from django.urls import path
from .views import(
    PingAPIView,
    UserRegisterAPIView,
    UserProfileAPIView,
    UserUpdatePasswordAPIView,
    UserDetailByLoginAPIView,
    UserFriendAddAPIView,
    UserFriendRemoveAPIView,
    UserFriendsListAPIView
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('ping/', PingAPIView.as_view(), name='server_operation_test'),
    path('auth/sign-in/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/register/', UserRegisterAPIView.as_view(), name='user_register'),
    path('me/profile/', UserProfileAPIView.as_view(), name='user_profile'),
    path('me/update_password/', UserUpdatePasswordAPIView.as_view(), name='user_update_password'),
    path('profiles/<str:login>/', UserDetailByLoginAPIView.as_view(), name='user_detail'),
    path('friends/', UserFriendsListAPIView.as_view(), name='user_friends_list'),
    path('friends/add/', UserFriendAddAPIView.as_view(), name='friend_add'),
    path('friends/remove/', UserFriendRemoveAPIView.as_view(), name='friend_remove')
]
