from rest_framework import permissions

class IsOwner(permissions.BasePermission):
   
    #Custom permission to only allow owners of an object to view, edit or delete it.

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request if the visibility of the board is PUBLIC,
        # so we'll always allow GET, HEAD, or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
          return obj.visibility == "public"

        # Write permissions are only allowed to the owner of the snippet.
        return obj.owner == request.user