from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, fields
from .model import ProductoModel
from categoria.serializer import CategoriaSerializer

class ProductoSerializer(SQLAlchemyAutoSchema):
    categoria = fields.Nested(
        nested=CategoriaSerializer, dump_only=True, only=('id', 'nombre'))
    class Meta:
        model = ProductoModel
        include_fk = True