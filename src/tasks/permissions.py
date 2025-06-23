from rest_framework import permissions

class IsManager(permissions.BasePermission):
    """
    Custom permission to only allow users with the 'is_manager' flag to access an endpoint.
    """

    def has_permission(self, request, view):
        # Check if the user is authenticated and if their profile has is_manager=True
        return request.user and request.user.is_authenticated and request.user.profile.is_manager


