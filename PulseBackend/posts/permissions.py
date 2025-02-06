class IsPostAccessiblePermission:
    def has_permission(self, request, view):
        """
        Always grants permission at the view level.
        """
        return True

    def has_object_permission(self, request, view, obj):
        if request.user == obj.author:
            return True

        if obj.author.is_public:
            return True

        if obj.author.friends.filter(id=request.user.id).exists():
            return True

        return False
