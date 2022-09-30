from rest_framework.permissions import IsAdminUser
from .permission import IsStaffEditorPermission

class StaffEditorPermissionMixin():
    permission_classes = [IsAdminUser, IsStaffEditorPermission]