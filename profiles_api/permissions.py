from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id


class UpdateOwnStatus(permissions.BasePermission):
    """Kullanıcıların yalnızca kendi status’larını güncelleyebilmesine izin verir"""

    def has_object_permission(self, request, view, obj):
        """Kullanıcının kendi status’unu güncelleyip güncellemediğini kontrol eder"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile.id == request.user.id
