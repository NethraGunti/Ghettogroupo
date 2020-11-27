from rest_framework import permissions


class HasTaskCreatePermissions(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.hasOwnerPerm() or request.user.hasAssignerPerm()

    def has_object_permission(self, request, view, obj):
        return request.user.hasOwnerPerm() or request.user.hasAssignerPerm()


class LimitObejectLevelView(permissions.BasePermission):
    
    def has_permission(self, request, view):
        if view.action not in ['list', 'create']:
            return False
        return request.user.hasOwnerPerm() or request.user.hasAssignerPerm()

