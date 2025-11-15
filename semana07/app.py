from flask import Flask, request, render_template
from dotenv import load_dotenv
from bd import conexion
from flask_migrate import Migrate
from os import environ
from modules.usuarios import usuarioBlueprint
from requests import post
from flask_jwt_extended import JWTManager
from datetime import timedelta
from cloudinary import config
from modules.multimedia import multimediaBlueprint
from flask_cors import CORS
load_dotenv()

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL')
# Para configurar nuestra JWT tenemos que setear el valor de esta variable
# https://flask-jwt-extended.readthedocs.io/en/stable/options.html
app.config['JWT_SECRET_KEY'] = environ.get('JWT_KEY')
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(
    hours=1, minutes=10, seconds=5)

conexion.init_app(app)

Migrate(app, conexion)
JWTManager(app)

config(cloudname=environ.get('CLOUDINARY_NAME'),
      api_key=environ.get('CLOUDINARY_API_KEY'),
      api_secret=environ.get('CLOUDINARY_API_SECRET'))


@app.route('/validar-usuario')
def validarUsuario():
    token = request.args.get('token')
    if not token:
        return render_template('not_found.html')

    # en nuestra API podemos consultar otras API's
    respuesta = post(
        'http://127.0.0.1:5000/usuario/habilitar-usuario', json={"token": token})
    if respuesta.status_code == 200:
        return render_template('validacion_exitosa.html')
    else:
        mensaje = respuesta.json().get('message')
        if mensaje and mensaje == 'El usuario ya esta validado, no se puede validar':
            return render_template('ya_esta_validado.html')

        return render_template('not_found.html')


app.register_blueprint(usuarioBlueprint)
app.register_blueprint(multimediaBlueprint)

if __name__ == '__main__':
    app.run(debug=True)