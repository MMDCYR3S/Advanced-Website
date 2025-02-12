from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """Description:
    BasePermission that allows only owner to have permissions to
    edit the object.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author.user == request.user
