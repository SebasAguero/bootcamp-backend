from bd import conexion
from sqlalchemy import Column, types

class CategoriaModel(conexion.Model):
    id = Column(type_=types.Integer, autoincrement=True, primary_key=True,
                    nullable=False)
    nombre = Column(type_=types.Text, nullable=False)
    posicion = Column(type_=types.Float, nullable=False)

    deletedAt = Column(type_=types.DateTime, name='deletedAt')

    __tablename__ = 'categorias'