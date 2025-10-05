from flask_restful import Api, request, Resource
from flask import Blueprint
from bd import conexion
from categoria import CategoriaModel
from .model import ProductoModel
from .serializer import ProductoSerializer
from marshmallow.exceptions import ValidationError

producto_blueprint = Blueprint('producto_bp', __name__)
producto_api = Api(producto_blueprint)


class Productos(Resource):
    serializador = ProductoSerializer()

    def get(self):
        print(request.args.get('status'))
        # En base al query param llamado status comportarse de la siguiente forma
        # all > entonces devolver disponibles y no disponibles
        # activos > entonces devolver disponibles
        # inactivos > entonces devolver no disponibles
        # si no se pasara el query param entonces devolver solo los disponibles
        # REALIZAR ESTAS OPERACIONES EN EL filter O filter_by
        status = request.args.get('status')
        filtro = {}

        if status is None:
            filtro = {'disponible': True}

        elif status == 'all':
            pass

        elif status == 'activos':
            filtro = {'disponible': True}

        elif status == 'inactivos':
            filtro = {'disponible': False}

        productos = conexion.session.query(
            ProductoModel).filter_by(**filtro).all()
        # 2da opcion
        # conexion.session.query(ProductoModel).filter(ProductoModel.disponible==True).all
        resultado = self.serializador.dump(productos, many=True)
        return {
            'message': 'Los productos son',
            'content': resultado
        }

    def post(self):
        data = request.get_json()
        try:
            dataValidada = self.serializador.load(data)

            categoriaId = dataValidada.get('categoriaId')
            if categoriaId:
                # Validar si hay categoria y si la categoria existe
                # SELECT id FROM categorias WHERE id = '' LIMIT 1;
                categoriaEncontrada = conexion.session.query(CategoriaModel).filter(
                    CategoriaModel.id == categoriaId).with_entities(CategoriaModel.id).first()

                if categoriaEncontrada is None:
                    return {
                        'message': 'Categoria no existe'
                    }, 400

            nuevoProducto = ProductoModel(**dataValidada)
            conexion.session.add(nuevoProducto)
            conexion.session.commit()
            resultado = self.serializador.dump(nuevoProducto)
            return {
                'message': 'Producto creado exitosamente',
                'content': resultado
            }, 201

        except ValidationError as error:
            return {
                'message': 'Error la crear el producto',
                'content': error.args
            }, 400


class Producto(Resource):
    serializador = ProductoSerializer()

    def get(self, id):
        productoEncontrado = conexion.session.query(
            ProductoModel).filter(ProductoModel.id == id).first()
        if not productoEncontrado:
            return {
                'message': 'Producto no encontrado'
            }, 404

        resultado = self.serializador.dump(productoEncontrado)

        return {
            'content': resultado
        }


producto_api.add_resource(Productos, '/productos')
producto_api.add_resource(Producto, '/producto/<int:id>')