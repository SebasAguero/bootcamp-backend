from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from marshmallow import Schema, fields
from .model import UsuarioModel


class RegistrarUsuarioSerializer(SQLAlchemyAutoSchema):
    # Modificar el serializador para indicar que la password sea load_only
    password = auto_field(load_only=True)

    class Meta:
        model = UsuarioModel

class HabilitarUsuarioSerializer(Schema):
    token = fields.Str(required=True)


class LoginSerializer(Schema):
    correo = fields.Email(required=True)
    password = fields.Str(required=True)

class PatchUsuarioSerializer (SQLAlchemyAutoSchema):
    #Solo lectura
    correo = auto_field(dump_only=True)
    validado = auto_field(dump_only=True)
    # Son opcionales
    nombre= auto_field(required=False)
    password = auto_field(required=False)

    class Meta:
        model = UsuarioModel