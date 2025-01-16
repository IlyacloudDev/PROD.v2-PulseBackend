from users.models import CustomUser


def _get_users():
    """
    Return a queryset of all users
    """
    return CustomUser.objects.all()


def _get_friends_of_user(pk):
    """
    Retrieve all friends of a user by their primary key.
    """
    user = CustomUser.objects.get(pk=pk)
    return user.friends.all()
