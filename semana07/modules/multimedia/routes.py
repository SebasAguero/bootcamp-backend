from flask_restful import Api
from flask import Blueprint
from .controller import GenerarLinkDeFoto, ActualizarFotoUsuario, DevolverMultimediaUrl

multimediaBlueprint = Blueprint('multimediaBlueprint', __name__)

multimediaRouter = Api(multimediaBlueprint, '/multimedia')

multimediaRouter.add_resource(GenerarLinkDeFoto, '/generar-upload-link')
multimediaRouter.add_resource(
    ActualizarFotoUsuario, '/actualizar-foto-usuario')
multimediaRouter.add_resource(
    DevolverMultimediaUrl, '/generar-url/<nombreImagen>')