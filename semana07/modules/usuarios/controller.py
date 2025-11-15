from flask_restful import request, Resource
from marshmallow.exceptions import ValidationError
from bcrypt import gensalt, hashpw, checkpw
from .serializer import RegistrarUsuarioSerializer, HabilitarUsuarioSerializer, LoginSerializer, PatchUsuarioSerializer
from .model import UsuarioModel
from bd import conexion
from utils import enviarCorreoDeValidacion
from cryptography.fernet import Fernet, InvalidToken
from os import environ
from ast import literal_eval
from flask_jwt_extended import create_access_token, jwt_required,  get_jwt_identity
from cloudinary import api


class RegistrarUsuario(Resource):
    serializer = RegistrarUsuarioSerializer()

    def post(self):
        data = request.get_json()
        try:

            dataSerializada = self.serializer.load(data)
            # Para generar el hash de nuestra password generamos el salt que es un texto aleatorio que se combinara con nuestra password
            salt = gensalt()
            # Convertimos la password a bytes
            password = dataSerializada.get('password')
            passwordByes = password.encode('utf-8')

            passwordHashed = hashpw(passwordByes, salt).decode('utf-8')
            # reemplazamos nuestra password original por el hashing de la password
            dataSerializada['password'] = passwordHashed

            nuevoUsuario = UsuarioModel(**dataSerializada)

            conexion.session.add(nuevoUsuario)
            conexion.session.commit()

            encriptador = Fernet(environ.get('FERNET_KEY'))
            informacion = {
                "id": nuevoUsuario.id
            }
            # Encripta la informacion y me la retorna en bytes por lo que la tenemos que decodificar para que sea un string
            token = encriptador.encrypt(
                str(informacion).encode('utf-8')).decode('utf-8')

            enviarCorreoDeValidacion(nuevoUsuario.correo, token)

            resultado = self.serializer.dump(nuevoUsuario)

            return {
                'message': 'Usuario registrado exitosamente',
                'content': resultado
            }, 201

        except ValidationError as error:
            return {
                'message': 'Error al crear el usuario',
                'content': error.args
            }, 400


class HabilitarUsuario(Resource):
    serializer = HabilitarUsuarioSerializer()

    def post(self):
        data = request.get_json()
        print(data)
        try:
            dataValidada = self.serializer.load(data)
            token = dataValidada.get('token')

            encriptador = Fernet(environ.get('FERNET_KEY'))
            informacionSecreta = encriptador.decrypt(token).decode('utf-8')
            # convertimos un str a un dict
            informacionSecretaDict = literal_eval(informacionSecreta)
            id = informacionSecretaDict.get('id')

            usuarioEncontrado = conexion.session.query(
                UsuarioModel).filter(UsuarioModel.id == id).first()

            if not usuarioEncontrado:
                return {
                    'message': 'Usuario no existe'
                }, 400
            # Actualizar el validado a True de ese usuario y agregar una condicional que si el usuario ya esta validado no se puede validar nuevamente
            if usuarioEncontrado.validado:
                return {
                    'message': 'El usuario ya esta validado, no se puede validar'
                }, 400

            conexion.session.query(UsuarioModel).filter(
                UsuarioModel.id == id).update({'validado': True})

            conexion.session.commit()

            return {
                'message': 'Usuario habilitado exitosamente'
            }
        except ValidationError as error:
            return {
                'message': 'Error al obtener la token',
                'content': error.args
            }, 400
        except InvalidToken as error:
            return {
                'message': 'Error al obtener la data de la token',
                'content': error.args
            }, 400


class Login(Resource):
    serializer = LoginSerializer()

    def post(self):
        data = request.get_json()
        try:
            # {'correo':'...', 'password': '...'}
            dataSerializada = self.serializer.load(data)

            usuarioEncontrado = conexion.session.query(UsuarioModel).filter(
                UsuarioModel.correo == dataSerializada.get('correo'), UsuarioModel.validado == True).first()

            if not usuarioEncontrado:
                return {
                    'message': 'Usuario no existe'
                }, 400

            # Validar las password
            # 1. Convertimos las passwords tanto la entrante como la almacena en la bd a bytes
            password = dataSerializada.get('password').encode('utf-8')
            passwordHasheada = usuarioEncontrado.password.encode('utf-8')

            # 2. Luego con el metodo checkpw validamos si son, esto retornara True | False
            resultado = checkpw(password, passwordHasheada)
            if resultado:
                # al momento de agregar informacion adicional NO UTILIZAR las llaves que son creadas por la libreria como exp, iat, nbf, jti, type, fresh
                informacionAdicional = {
                    'nombre': usuarioEncontrado.nombre, 'correo': usuarioEncontrado.correo
                }

                # el identificador de la token tiene que ser un string, no puede ser un numero
                token = create_access_token(
                    identity=str(usuarioEncontrado.id), additional_claims=informacionAdicional)

                return {
                    'message': 'Bienvenido',
                    'content': token
                }
            else:
                return {
                    'message': 'Credenciales incorrectas'
                }, 400
        except ValidationError as error:
            return {
                'message': 'Error al hacer el login',
                'content': error.args
            }, 400


class Perfil(Resource):
    serializador = RegistrarUsuarioSerializer()

    # Indica que para poder acceder a este metodo se necesite de manera obligatoria una token en los headers
    @jwt_required()
    def get(self):
        # me retornara el identificador del usuario que esta accediendo a este controlador, si no hay, su valor sera None
        identificador = get_jwt_identity()
        print(identificador)
        usuarioEncontrado = conexion.session.query(UsuarioModel).filter(
            UsuarioModel.id == identificador).first()

        resultado = self.serializador.dump(usuarioEncontrado)
        return {
            'content': resultado
        }

    # put > para actualizaciones totales (todo el registro)
    # patch > actualizaciones parciales (solamente uno o varios campos mas no obligatoriamente todos)
    @jwt_required()
    def patch(self):
        identificador = get_jwt_identity()
        serializador = PatchUsuarioSerializer()
        # actualizar SOLAMENTE el nombre y password, y si envia la password generar el hashing nuevamente
        try:
            dataValidada = serializador.load(request.get_json())
            # SELECT id FROM usuarios WHERE id ='...';
            usuarioEncontrado = conexion.session.query(UsuarioModel).filter(
                UsuarioModel.id == identificador).with_entities(UsuarioModel.id).first()

            if not usuarioEncontrado:
                return {
                    'message': 'Usuario no existe'
                }, 400

            nuevaInfo = {}

            if dataValidada.get('nombre'):
                nuevaInfo['nombre'] = dataValidada.get('nombre')

            if dataValidada.get('password'):
                salt = gensalt()
                nuevaPassword = dataValidada.get('password').encode('utf-8')
                passwordHasheada = hashpw(nuevaPassword, salt).decode('utf-8')
                nuevaInfo['password'] = passwordHasheada

            conexion.session.query(UsuarioModel).filter(
                UsuarioModel.id == identificador).update(nuevaInfo)
            conexion.session.commit()

            return {
                'message': 'Usuario actualizado exitosamente',
                'content': ''
            }

        except ValidationError as error:
            return {
                'message': 'Error al actualizar el usuario',
                'content': error.args
            }, 400