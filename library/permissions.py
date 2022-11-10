from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow Admin of an object to edit it. 
    STILL NEEDS TO BE DONE
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # # Write permissions are only allowed to the owner of the snippet.
        # return obj.user == request.user

# NEED A IS OWNER OF READ ONLY SO I CAN PUT IT ON NOTES AND TRACK