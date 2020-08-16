from rest_framework.permissions import BasePermission

class IsSuperUser(BasePermission):
    
    message = 'User is not a superuser'

    def has_permission(self, request, view):
        
        has_permission = False
        user = request.user
        if user.is_staff and user.is_superuser:
            has_permission = True
        return has_permission

class IsStaff(BasePermission):
    
    message = 'User is not an employee'

    def has_permission(self, request, view):
        
        has_permission = False
        user = request.user
        if user.is_staff:
            has_permission = True
        return has_permission

class IsOwner(BasePermission):
    
    message = 'User is not the owner of this customer account'

    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        
        has_permission = False
        if request.user.id == obj.id or request.user.is_staff:
            has_permission = True
        return has_permission

class IsStaffOwner(BasePermission):
    
    message = 'User is not the owner of this employee account'

    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        
        has_permission = False
        if request.user.id == obj.id or (request.user.is_staff and request.user.is_superuser):
            has_permission = True
        return has_permission

class IsClientOwner(BasePermission):

    """
    permission to only allow owners of an auditor account to list its relations.
    """
    message = "user making the request is not the owner of this account"

    def has_permission(self, request, view):
        has_permission = False
        if not request.user.is_staff:
            if request.user.id == (int)(view.kwargs["client_pk"]):
                has_permission = True
                if view.action == "create" and "client" in request.data and not (int)(request.data["customer"]) == request.user.id:
                    has_permission = False
                    self.message = "Customer sent in data is not the same customer on url"
            elif request.user.is_superuser:
                has_permission = True
            else:
                has_permission = False
        return has_permission