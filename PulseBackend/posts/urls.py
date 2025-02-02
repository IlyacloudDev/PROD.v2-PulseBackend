from django.urls import path
from .views import PostCreateAPIView


urlpatterns = [
    path("new/", PostCreateAPIView.as_view(), name='post_create')
]
