from rest_framework.generics import CreateAPIView, RetrieveAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .serializers import PostCreateOrGetSerializer, PostLikeDislikeSerializer
from .permissions import IsPostAccessiblePermission
from .services.posts_serializers_views import _get_posts, _get_posts_of_author, _get_post_by_id
from .paginations import PostListPagination


class PostCreateAPIView(CreateAPIView):
    """
    Handles creating a new post.
    Requires authentication and automatically assigns the author.
    """
    serializer_class = PostCreateOrGetSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        """
        Add the author (current user) to the serializer context.
        """
        context = super().get_serializer_context()
        context['author'] = self.request.user
        return context


class PostDetailByIdAPIView(RetrieveAPIView):
    """
    Handles receiving an instance of a post.
    """
    queryset = _get_posts()
    serializer_class = PostCreateOrGetSerializer
    permission_classes = [IsAuthenticated, IsPostAccessiblePermission]


class PostListAPIView(ListAPIView):
    """
    Handles receiving list of current user posts
    """
    serializer_class = PostCreateOrGetSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = PostListPagination

    def get_queryset(self):
        return _get_posts_of_author(author_pk=self.request.user.id)


class PostListByLoginAPIView(ListAPIView):
    """
    Handles retrieving a list of posts created by a specific user based on their login.
    Access is granted only if the authenticated user is a friend of the requested user.
    """
    serializer_class = PostCreateOrGetSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = PostListPagination

    def get_queryset(self):
        """Retrieve posts of the specified user if they are a friend of the requester."""
        login = self.kwargs.get('login')
        return _get_posts_of_author(login=login, request=self.request)


class BasePostLikeDislikeAPIView(CreateAPIView):
    """
    Handles like and dislike actions on a post.
    """
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        """
        Handle the creation of a like or dislike action.
        """
        response = super().create(request, *args, **kwargs)

        if response.status_code == 201:
            return Response(response.data, status=status.HTTP_200_OK)

        return response

    def get_serializer_context(self):
        """
        Add 'post' and 'action' to the serializer context.
        """
        context = super().get_serializer_context()

        post_id = self.kwargs.get('pk')
        context['post'] = _get_post_by_id(request=self.request, post_id=post_id)
        context['action'] = self.action
        return context


class PostLikeAPIView(BasePostLikeDislikeAPIView):
    """
    Handles liking of post.
    """
    serializer_class = PostLikeDislikeSerializer
    action = 'like'


class PostDislikeAPIView(BasePostLikeDislikeAPIView):
    """
    Handles disliking of post.
    """
    serializer_class = PostLikeDislikeSerializer
    action = 'dislike'
