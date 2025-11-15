from flask_restful import Api
from flask import Blueprint
from .controller import RegistrarUsuario, HabilitarUsuario, Login, Perfil

usuarioBlueprint = Blueprint('usuarioBlueprint', __name__)
# El prefijo indica que todas las rutas declaradas dentro de esta Api empezaran con `/usuario/....`
usuarioApi = Api(usuarioBlueprint, '/usuario')

# Declararemos todas las rutas para los controladores del usuario
usuarioApi.add_resource(RegistrarUsuario, '/registro')
usuarioApi.add_resource(HabilitarUsuario, '/habilitar-usuario')
usuarioApi.add_resource(Login, '/login')
usuarioApi.add_resource(Perfil, '')