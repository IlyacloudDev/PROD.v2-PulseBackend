from rest_framework.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from posts.models import Post


def _validation_provided_tag(value):
    """
    Validate the provided tags.
    Ensures tags are a list of strings with a maximum length of 20 characters.
    """
    if not isinstance(value, list):
        raise ValidationError(_("Tags field must be list"))
    for tag in value:
        if not isinstance(tag, str) or len(tag) > 20:
            raise ValidationError(_("Tag must be string between 0 and 20 characters"))
    return value


def _create_new_post_instance_with_provided_data(validated_data, author):
    """
    Create and save a new post instance with the given validated data.
    """
    post = Post(**validated_data, author=author)
    post.save()
    return post
