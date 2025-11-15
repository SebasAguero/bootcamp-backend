from sqlalchemy import Column, types
from bd import conexion
from datetime import datetime

class UsuarioModel(conexion.Model):
    id = Column(type_=types.Integer, autoincrement=True, primary_key=True)
    nombre = Column(type_=types.Text, nullable=False)
    correo = Column(type_=types.Text, nullable=False, unique=True)
    password = Column(type_=types.Text, nullable=False)
    validado = Column(type_=types.Boolean, default=False)
    # Auditoria (Validar los registros en base a sus fechas de creacion y actualizacion)
    createdAt = Column(
        type_=types.DateTime, default=datetime.now, name='created_at')
    # cuando se actualice cualquier columna del registro se modifique el valor de esta columna a la fecha y hora actual
    updatedAt = Column(type_=types.DateTime,
                      default=datetime.now, onupdate=datetime.now, name='updated_at')

    __tablename__ = 'usuarios'
