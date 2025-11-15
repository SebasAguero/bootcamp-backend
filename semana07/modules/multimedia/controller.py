from flask_restful import Resource, request
from cloudinary import utils
from datetime import datetime
from os import environ
from .serializer import GenerarLinkSerializer, ActualizarFotoUsuarioSerializer
from marshmallow import ValidationError
from ..usuarios import UsuarioModel
from .model import MultimediaModel
from flask_jwt_extended import jwt_required, get_jwt_identity
from uuid import uuid4

from bd import conexion


class GenerarLinkDeFoto(Resource):
    @jwt_required()
    def post(self):
        serializador = GenerarLinkSerializer()
        try:
            dataValidada = serializador.load(request.get_json())
            timestamp = round(datetime.now().timestamp())

            # Generar UUID único
            unique_id = str(uuid4())
            public_id = f"{unique_id}_{dataValidada.get('fileName')}"

            parametros = {
                'timestamp': timestamp,
                'folder': dataValidada.get('folder'),
                'public_id': public_id
            }

            signature = utils.api_sign_request(
                parametros, environ.get('CLOUDINARY_API_SECRET'))
            apiKey = environ.get('CLOUDINARY_API_KEY')
            cloudName = environ.get('CLOUDINARY_NAME')
            folder = dataValidada.get('folder')
            cloudinaryUrl = 'https://api.cloudinary.com/v1_1'

            return {
                'content': {
                    'signature': signature,
                    'timestamp': timestamp,
                    'apiKey': apiKey,
                    'url': f'{cloudinaryUrl}/{cloudName}/image/upload',
                    'folder': folder,
                    'public_id': public_id
                }
            }

        except ValidationError as error:
            return {
                'message': 'Error al generar el link',
                'content': error.args
            }, 400


class ActualizarFotoUsuario(Resource):
    @jwt_required()
    def put(self):
        usuarioId = get_jwt_identity()
        serializer = ActualizarFotoUsuarioSerializer()

        try:
            data = request.get_json()
            data['usuarioId'] = usuarioId
            dataValidada = serializer.load(data)

            # Verificar que el usuario exista y esté validado
            usuarioEncontrado = conexion.session.query(UsuarioModel).filter(
                UsuarioModel.id == usuarioId, UsuarioModel.validado == True
            ).with_entities(UsuarioModel.id).first()

            if not usuarioEncontrado:
                return {
                    'message': 'Usuario no existe o no está validado'
                }, 400

            # Verificar si ya existe una multimedia para este usuario
            multimedia_existente = conexion.session.query(MultimediaModel).filter(
                MultimediaModel.usuarioId == usuarioId
            ).first()

            if multimedia_existente:
                # Actualizar registro existente
                for key, value in dataValidada.items():
                    setattr(multimedia_existente, key, value)
                conexion.session.commit()
                resultado = serializer.dump(multimedia_existente)
            else:
                # Crear nueva multimedia
                nuevaMultimedia = MultimediaModel(**dataValidada)
                conexion.session.add(nuevaMultimedia)
                conexion.session.commit()
                resultado = serializer.dump(nuevaMultimedia)

            return {
                'message': 'Foto actualizada exitosamente',
                'content': resultado
            }, 201

        except ValidationError as error:
            return {
                'message': 'Error al actualizar la foto del usuario',
                'content': error.args
            }, 400


class DevolverMultimediaUrl(Resource):
    @jwt_required()
    def get(self, nombreImagen):
        parametros = {
            'source': f'pruebas/{nombreImagen}',
            'cloud_name': environ.get('CLOUDINARY_NAME'),
            'resource_type': 'image',
            'secure': True,
            'transformation': [{'width': 400, 'height': 400, 'crop': 'fill', 'effect': "vignette"}]
        }

        resultado = utils.cloudinary_url(**parametros)

        return {
            'url': resultado[0]
        }