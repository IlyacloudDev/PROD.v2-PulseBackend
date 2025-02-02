from django.db import models
from users.models import CustomUser
from django.core.validators import MinValueValidator
from django.utils.translation import gettext_lazy as _


class Post(models.Model):
    """
    Model representing a user's post with content, tags, and likes/dislikes count.
    """
    content = models.TextField(
        verbose_name=_("Content"),
        max_length=1000,
        help_text=_("The content of the post (up to 1000 characters).")
    )
    author = models.ForeignKey(
        CustomUser,
        to_field="login",
        on_delete=models.CASCADE,
        related_name="posts",
        verbose_name=_("Author"),
        help_text=_("The user who created this post.")
    )
    tags = models.JSONField(
        verbose_name=_("Tags"),
        default=list,
        help_text=_("A list of tags associated with this post.")
    )
    created_at = models.DateTimeField(
        verbose_name=_("Created At"),
        auto_now_add=True,
        help_text=_("The date and time when the post was created.")
    )
    likes_count = models.IntegerField(
        verbose_name=_("Likes Count"),
        default=0,
        validators=[MinValueValidator(0)],
        help_text=_("The number of likes this post has received.")
    )
    liked_users = models.ManyToManyField(
        CustomUser,
        related_name="liked_posts",
        verbose_name=_("Liked Users"),
        help_text=_("Users who liked the post")
    )
    dislikes_count = models.IntegerField(
        verbose_name=_("Dislikes Count"),
        default=0,
        validators=[MinValueValidator(0)],
        help_text=_("The number of dislikes this post has received.")
    )
    disliked_users = models.ManyToManyField(
        CustomUser,
        related_name="disliked_posts",
        verbose_name=_("Disliked Users"),
        help_text=_("Users who disliked the post")
    )

    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")

    def __str__(self):
        """
        Returns the post content's first 30 characters as its string representation.
        """
        return self.content[:30]
