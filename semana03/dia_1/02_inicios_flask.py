from flask import Flask

servidor = Flask(__name__)

@servidor.route('/')
def bienvenida():
  return 'Bienvenido a mi API de Flask'

# frontend 8080
# postgres 5432
servidor.run(port=5000,debug=True)