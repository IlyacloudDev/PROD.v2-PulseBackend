from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from .serializers import PostCreateSerializer


class PostCreateAPIView(CreateAPIView):
    """
    Handles creating a new post.
    Requires authentication and automatically assigns the author.
    """
    permission_classes = [IsAuthenticated]
    serializer_class = PostCreateSerializer

    def get_serializer_context(self):
        """
        Add the author (current user) to the serializer context.
        """
        context = super().get_serializer_context()
        context['author'] = self.request.user
        return context
