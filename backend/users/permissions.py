from rest_framework.permissions import BasePermission


class IsActiveUser(BasePermission):
    '''
    Ограничение доступа для временно удаленного пользователя
    '''
    def has_permission(self, request, view):
        return request.user.is_active