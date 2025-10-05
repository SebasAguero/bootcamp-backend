from flask import Flask, render_template
from bd import conexion
from os import environ
from dotenv import load_dotenv
from categoria import categorias_blueprint, CategoriaModel
from producto import producto_blueprint
from flask_migrate import Migrate
from flask_cors import CORS

load_dotenv()

app = Flask(__name__)
# methods > GET | POST | PUT | DELETE | PATCH
# origins > que clientes pueden acceder a mi API (*)
# headers > que cabeceras pueden enviarse (*)
CORS(app, origins=['http://localhost:5173'],
    methods=['GET', 'POST', 'PUT', 'DELETE'])
# Se almacenan variables que sirve para el funcionamiento de la aplicacion, no son las mismas  que las variables de entorno
# print(app.config)

# agregamos la variable que necesita SQLALChemy para funcionar
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL')

# Inicializamos nuestra conexion a la bd
conexion.init_app(app)

# Luego de inicializar mi conexion con la bd creamos el flujo de migracion
Migrate(app, conexion)


@app.route('/')
def inicio():
    data = [{"id": 1, "nombre": "Eduardo", "edad": 21},
            {"id": 2, "nombre": "Luis", "edad": 18},
            {"id": 3, "nombre": "Sebastian", "edad": 19}]

    categorias = conexion.session.query(CategoriaModel).all()
    print(categorias)
    # Mostrar en una tabla todas las categorias y las que estan eliminadas colocar una columna ELIMINADO
    return render_template('inicio.html', nombre='Backend G-26', data=data, categorias=categorias)


# Aca registraremos los mini-apps en nuestra aplicacion principal
app.register_blueprint(categorias_blueprint)
app.register_blueprint(producto_blueprint)

if (__name__ == '__main__'):
    app.run(debug=True)