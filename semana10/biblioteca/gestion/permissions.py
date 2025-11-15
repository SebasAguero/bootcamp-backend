from rest_framework.permissions import BasePermission

class EsAdmin(BasePermission):
    message = 'No tienes los privilegios suficientes para realizar esta acción.'
    def has_permission(self, request, view):
        if not request.user:
            return False
        if request.method == 'GET':
            return True
        tipoUsuario = request.user.tipoUsuario

        return tipoUsuario == '1'
    
class EsPersonal(BasePermission):
    message = 'No tienes los privilegios suficientes para realizar esta acción.'
    def has_permission(self, request, view):

        if request.method == 'GET':
            return True
        tipoUsuario = request.user.tipoUsuario

        return tipoUsuario == '2'