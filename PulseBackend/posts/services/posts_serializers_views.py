from posts.models import Post
from django.shortcuts import get_object_or_404
from users.models import CustomUser
from django.http import Http404


def _get_posts():
    """
    Return a queryset of all posts
    """
    return Post.objects.all()


def _get_posts_of_author(request=None, author_pk=None, login=None):
    """
    Retrieve posts of a specific author.
    """
    if login:
        author = get_object_or_404(CustomUser, login=login)
        if author.friends.filter(id=request.user.id).exists() or author == request.user or author.is_public:
            return Post.objects.filter(author=author).order_by('-created_at')
        else:
            raise Http404

    return Post.objects.filter(author__pk=author_pk).order_by('-created_at')


def _get_post_by_id(request, post_id):
    """
    Retrieve posts of a specific author.
    """
    post = get_object_or_404(Post, pk=post_id)
    post_author = post.author
    if post_author.friends.filter(id=request.user.id).exists() or post_author == request.user or post_author.is_public:
        return post
    else:
        raise Http404

