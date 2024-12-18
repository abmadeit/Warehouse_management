from rest_framework.permissions import BasePermission

# Custom permission for Admin
class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.role.name == 'ADMIN'

# Custom permission for Manager
class IsManager(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.role.name == 'MANAGER'

# Custom permission for Operator
class IsOperator(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.role.name == 'OPERATOR'
