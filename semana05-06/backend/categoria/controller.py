from flask_restful import Resource, Api, request
from flask import Blueprint
from .model import CategoriaModel
from bd import conexion
from .serializer import CategoriaSerializer, ReordenarCategoriaSerializer
from marshmallow.exceptions import ValidationError
from datetime import datetime
# Ahora registraremos nuestro blueprint (mini aplicacion de categorias)
categorias_blueprint = Blueprint('categorias_bp', __name__)

# Con la clase Api nosotros declaramos los recursos de los controladores como los recursos a ser consumidos en nuestra aplicacion de flask
categoria_api = Api(categorias_blueprint)


# Al momento de heredar la clase Resource ahora los metodos http que declaremos como metodos de la clase serviran para poderlos consumir como metodos http
class Categorias(Resource):
    # Este sera un atributo que podra ser usado en todos los metodos de mi clase
    serializador = CategoriaSerializer()

    def get(self):
        # Asi se utiliza el ORM
        # SELECT * FROM categorias WHERE deleted_at IS NULL;
        categorias = conexion.session.query(CategoriaModel).filter(
            CategoriaModel.deletedAt == None).order_by(CategoriaModel.posicion.asc()).all()

        resultado = self.serializador.dump(categorias, many=True)

        return {
            'message': 'Las categorias son',
            'content': resultado
        }

    def post(self):
        body = request.get_json()
        try:
            # { "nombre": "Entradas", "orden": 2 }
            dataSerializada = self.serializador.load(body)
            # CategoriaModel(nombre=dataSerializada.get('nombre'),
            #                orden=dataSerializada.get('orden'))

            # encontraremos la ultima posicion de la categoria
            # SELECT orden FROM categorias ORDER BY orden DESC;
            ultimaPosicion = conexion.session.query(CategoriaModel).order_by(
                CategoriaModel.posicion.desc()).with_entities(CategoriaModel.posicion).first()

            # Operador ternario
            # VALOR_SI_ES_VERDADERO if CONDICION else VALOR_SI_ES_FALSO
            posicion = ultimaPosicion[0] + 1 if ultimaPosicion and len(
                ultimaPosicion) == 1 else 1

            # aqui agregamos el orden con el calculo de la ultima posicion
            dataSerializada['posicion'] = posicion

            # ** en paso de parametros lo que hace es convierte el diccionario a sus llaves las vuelve los parametros y sus valores a los valores de esos parametros
            nuevaCategoria = CategoriaModel(**dataSerializada)
            # Añadimos a la conexion nuestra nueva categoria
            conexion.session.add(nuevaCategoria)
            # Guardamos de manera permanente nuestra nueva categoria en la bd
            conexion.session.commit()
            # dump agarra la instancia del registro y lo convierte a un diccionario
            resultado = self.serializador.dump(nuevaCategoria)

            return {
                'message': 'Categoria creada exitosamente',
                'content': resultado
            }, 201
        except ValidationError as error:
            return {
                'message': 'Error al crear la categoria',
                'content': error.args
            }


# /categoria/:id
class Categoria(Resource):
    serializador = CategoriaSerializer()

    def get(self, id):
        # SELECT * FROM categorias WHERE id = '' LIMIT 1;
        categoriaEncontrada = conexion.session.query(
            CategoriaModel).filter(CategoriaModel.id == id).first()

        if not categoriaEncontrada:
            return {
                'message': 'La categoria no existe'
            }, 404  # not found

        result = self.serializador.dump(categoriaEncontrada)

        return {
            'content': result
        }, 200  # ok (por defecto si no se le pone nada)

    def delete(self, id):
        # SELECT id FROM categorias WHERE id = '' AND deleted_at IS NULL;
        categoriaEncontrada = conexion.session.query(CategoriaModel).filter(
            CategoriaModel.id == id,
            CategoriaModel.deletedAt == None).with_entities(CategoriaModel.id).first()

        if categoriaEncontrada is None:
            return {
                'message': 'Categoria no existe'
            }, 404

        # Asi se realiza el update de los elementos de la tabla Categorias
        # UPDATE categorias SET deleted_at = '' WHERE id = '';
        conexion.session.query(CategoriaModel).filter(CategoriaModel.id == id).update(
            {CategoriaModel.deletedAt: datetime.now()})

        conexion.session.commit()

        return {
            'message': 'Categoria eliminada con exito'
        }

    def put(self, id):
        body = request.get_json()
        try:
            categoriaEncontrada = conexion.session.query(CategoriaModel).filter(
                CategoriaModel.deletedAt == None).with_entities(CategoriaModel.id).first()

            if not categoriaEncontrada:
                return {
                    'message': 'Categoria no existe'
                }, 404

            dataValidada = self.serializador.load(body)

            conexion.session.query(CategoriaModel).filter(
                CategoriaModel.id == id).update(dataValidada)

            # el metodo get hace que la busqueda sea mas optima ya que solamente buscara por las columnas indexadas haciendo que sea mejor siempre y cuando la columna a buscar este indexada (es unique o primary key)
            categoriaActualizada = conexion.session.query(
                CategoriaModel).get(id)

            conexion.session.commit()

            resultado = self.serializador.dump(categoriaActualizada)

            return {
                'message': 'Categoria actualizada exitosamente',
                'content': resultado
            }

        except ValidationError as error:
            return {
                'message': 'Error al actualizar la categoria',
                'content': error.args
            }, 400


class ReordenarCategoria(Resource):
    def post(self):
        data = request.get_json()
        serializador = ReordenarCategoriaSerializer()
        try:
            dataSerializada = serializador.load(data)
            categoriaId = dataSerializada.get('categoriaId')
            idVecinoAnterior = dataSerializada.get('idVecinoAnterior')
            idVecinoProximo = dataSerializada.get('idVecinoProximo')
            print(idVecinoProximo)
            nuevaPosicion = 0
            # Si hay vecinoAnterior y vecinoProximo entonces se debe acomodar entre esos dos
            if idVecinoAnterior and idVecinoProximo:
                vecinoAnterior = conexion.session.query(
                    CategoriaModel).filter(CategoriaModel.id == idVecinoAnterior).first()
                vecinoProximo = conexion.session.query(
                    CategoriaModel).filter(CategoriaModel.id == idVecinoProximo).first()

                posicionVecinoAnterior = vecinoAnterior.posicion
                posicionVecinoProximo = vecinoProximo.posicion

                nuevaPosicion = (posicionVecinoAnterior +
                                posicionVecinoProximo)/2
            # Si solo hay vecinoAnterior entonces va al final de la lista
            elif idVecinoAnterior:
                vecinoAnterior = conexion.session.query(
                    CategoriaModel).filter(CategoriaModel.id == idVecinoAnterior).first()
                posicionVecinoAnterior = vecinoAnterior.posicion
                nuevaPosicion = posicionVecinoAnterior + 1
            # Si solo hay vecinoProximo entonces va al inicio de la lista
            elif idVecinoProximo:
                vecinoProximo = conexion.session.query(
                    CategoriaModel).filter(CategoriaModel.id == idVecinoProximo).first()
                posicionVecinoProximo = vecinoProximo.posicion
                nuevaPosicion = posicionVecinoProximo / 2

            conexion.session.query(CategoriaModel).filter(
                CategoriaModel.id == categoriaId).update({'posicion': nuevaPosicion})

            conexion.session.commit()

            return {
                'message': 'Categoria actualizada exitosamente'
            }
        except ValidationError as error:
            return {
                'message': 'Error al cambiar el orden de la categoria',
                'content': error.args
            }, 400


# Luego de haber declarado todos nuestros Recursos ahora agregaremos esos recursos a nuestra Api
categoria_api.add_resource(Categorias, '/categorias')
categoria_api.add_resource(Categoria, '/categoria/<int:id>')
categoria_api.add_resource(ReordenarCategoria, '/categoria/cambiar-orden')