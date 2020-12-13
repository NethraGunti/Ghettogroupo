from rest_framework import permissions


class HasTaskCreatePermissions(permissions.BasePermission):

    def has_permission(self, request, view):
        if view.action not in ['list', 'retrieve']:
            return request.user.hasOwnerPerm() or request.user.hasAssignerPerm() or request.user.hasDeveloperPerm()
        return True

    def has_object_permission(self, request, view, obj):
        if view.action not in ['list', 'retrieve']:
            return request.user.hasOwnerPerm() or request.user.hasAssignerPerm() or request.user.hasDeveloperPerm()
        return True


class LimitObejectLevelView(permissions.BasePermission):

    def has_permission(self, request, view):
        if view.action not in ['list', 'create']:
            return False
        return request.user.hasOwnerPerm() or request.user.hasAssignerPerm() or request.user.hasDeveloperPerm()