from bd import conexion
from sqlalchemy import Column, types, ForeignKey
from sqlalchemy.orm import relationship

class ProductoModel(conexion.Model):
    id = Column(type_ = types.Integer, autoincrement=True, primary_key=True)
    nombre = Column(type_ = types.Text, nullable=False)
    precio = Column(type_ = types.Float, nullable=False)
    descripcion = Column(type_ = types.Text)
    disponible = Column(type_ = types.Boolean, default=True)

    categoriaId = Column(ForeignKey(column='categorias.id'),
                        nullable=True, name='categoria_id')

    __tablename__ = 'productos'