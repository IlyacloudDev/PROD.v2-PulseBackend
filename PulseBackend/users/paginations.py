from rest_framework.pagination import LimitOffsetPagination


class FriendsListPagination(LimitOffsetPagination):
    """
    Custom pagination class for paginating friends list.
    """
    default_limit = 5
    limit_query_param = 'page_size'
    offset_query_param = 'offset'
