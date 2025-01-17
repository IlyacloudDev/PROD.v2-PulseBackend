class IsProfileAccessiblePermission:
    """
    Permission class to determine if the user can access the profile.
    """
    def has_permission(self, request, view):
        """
        Always grants permission at the view level.
        """
        return True

    def has_object_permission(self, request, view, obj):
        """
        Grants access if the user is the profile owner, the profile is public,
        or the user is a friend of the profile owner.
        """
        if request.user == obj:
            return True

        if obj.is_public:
            return True

        if obj.friends.filter(id=request.user.id).exists():
            return True

        return False
