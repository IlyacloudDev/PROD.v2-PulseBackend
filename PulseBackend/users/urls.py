from django.urls import path
from .views import PingAPIView, UserRegisterAPIView, UserProfileAPIView, UserUpdatePasswordAPIView
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
    path('me/update_password/', UserUpdatePasswordAPIView.as_view(), name='user_update_password')
]
