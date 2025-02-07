from django.urls import path
from .views import PostCreateAPIView, PostDetailByIdAPIView, PostListAPIView, PostListByLoginAPIView, PostLikeAPIView, PostDislikeAPIView


urlpatterns = [
    path('new/', PostCreateAPIView.as_view(), name='post_create'),
    path('<int:pk>/', PostDetailByIdAPIView.as_view(), name='post_get_instance'),
    path('feed/my/', PostListAPIView.as_view(), name='post_get_list'),
    path('feed/<str:login>/', PostListByLoginAPIView.as_view(), name='post_get_list_by_login'),
    path('<int:pk>/like/', PostLikeAPIView.as_view(), name='post_like'),
    path('<int:pk>/dislike/', PostDislikeAPIView.as_view(), name='post_dislike')
]
