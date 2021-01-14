from rest_framework.permissions import BasePermission


class CanViewAPIPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('staff.can_view_api')
