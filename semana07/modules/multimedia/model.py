from bd import conexion
from sqlalchemy import Column, types, ForeignKey


class MultimediaModel(conexion.Model):
    id = Column(type_=types.Integer, autoincrement=True, primary_key=True)
    fileName = Column(type_=types.String, nullable=False, name='file_name')
    extension = Column(type_=types.String, nullable=False)
    contentType = Column(type_=types.String,
                        nullable=False, name='content_type')
    folder = Column(type_=types.String, nullable=False)

    usuarioId = Column(ForeignKey(column='usuarios.id'),
                      nullable=True, name='usuario_id')

    __tablename__ = 'multimedias'