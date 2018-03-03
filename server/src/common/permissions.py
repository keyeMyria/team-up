from django.contrib.auth import get_user_model
from rest_framework.permissions import SAFE_METHODS, BasePermission
from rest_framework.request import Request

from games.models import GameAccount


class IsOwnerOrAdminOrReadOnly(BasePermission):
    def has_object_permission(self, request: Request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        else:
            if isinstance(obj, get_user_model()):
                user = obj
            elif isinstance(obj, GameAccount):
                user = obj.user_profile.user
            else:
                user = obj.user
            return request.user.is_superuser or request.user == user


class IsOwnerOrAdmin(BasePermission):
    def has_object_permission(self, request: Request, view, obj):
        return request.user == obj.user or request.user.is_superuser


def is_admin(user):
    return user.is_superuser
