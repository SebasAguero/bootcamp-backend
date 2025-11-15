from marshmallow import Schema, fields, validate
from enum import Enum
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from .model import MultimediaModel


class AllowedExtensionEnum(Enum):
    gif = 'gif'
    jpg = 'jpg'
    jpeg = 'jpeg'
    png = 'png'


allowedContentType = [
    'image/gif',
    'image/jpeg',
    'image/jpg',
    'image/png']


class GenerarLinkSerializer(Schema):
    # mi_foto
    fileName = fields.Str(required=True)

    # jpg
    extension = fields.Enum(enum=AllowedExtensionEnum, required=True)

    # mimetype (estandar que sirve para indicar que tipo de archivo es) image/jpeg
    contentType = fields.Str(validate=validate.OneOf(
        allowedContentType, error='Valor incorrecto, solo se admiten: {choices}'), required=True)

    # usuarios/
    folder = fields.Str(required=False)


class ActualizarFotoUsuarioSerializer(SQLAlchemyAutoSchema):
    usuarioId = auto_field(required=True)

    class Meta:
        model = MultimediaModel
        include_fk = True