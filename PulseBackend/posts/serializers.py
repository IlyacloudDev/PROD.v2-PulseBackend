from rest_framework import serializers
from .models import Post
from .services.posts_serializers_services import _validation_provided_tag, _create_new_post_instance_with_provided_data


class PostCreateSerializer(serializers.ModelSerializer):
    """
    Serializer for creating a post.
    Ensures proper validation of input data, including tag validation.
    """
    author = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Post
        fields = ['id', 'content', 'author', 'tags', 'created_at', 'likes_count', 'dislikes_count']
        extra_kwargs = {
            'id': {'read_only': True},
            'created_at': {'read_only': True},
            'likes_count': {'read_only': True},
            'dislikes_count': {'read_only': True},
        }

    def get_author(self, obj):
        """Retrieve the author's login."""
        return obj.author.login

    def validate_tags(self, value):
        """Validate the provided tags before saving."""
        return _validation_provided_tag(value=value)

    def create(self, validated_data):
        """Create a new post instance with the provided data."""
        author = self.context['author']
        return _create_new_post_instance_with_provided_data(validated_data=validated_data, author=author)

