from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from marshmallow import Schema, fields
from .model import CategoriaModel

class CategoriaSerializer(SQLAlchemyAutoSchema):

    posicion = auto_field(dump_only=True)

    class Meta:
        model = CategoriaModel

class ReordenarCategoriaSerializer(Schema):
    categoriaId = fields.Int(required=True)
    idVecinoAnterior = fields.Int(required=False)
    idVecinoProximo = fields.Int(required=False)