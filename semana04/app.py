from flask import Flask, request
from psycopg import connect
from dotenv  import load_dotenv
from os import environ
from marshmallow import Schema, fields
from marshmallow.exceptions import ValidationError
from psycopg.rows import dict_row

load_dotenv()

class CanchaSchema(Schema):
      id = fields.Int(dump_only=True)
      nombre = fields.Str(required=True)
      disponible = fields.Bool(required=False)

class ReservaSchema(Schema):
    id = fields.Int(dump_only=True)
    nombre = fields.Str(required=True)
    horaInicio = fields.Time(required=True, format='%H:%M')
    horaFin = fields.Time(required=True, format='%H:%M')
    adelanto = fields.Float(required=False)
    total = fields.Float(required=True)
    canchaId = fields.Int(required=True, data_key="canchaId")

app = Flask (__name__)
conn = connect(environ.get('DATABASE_URL',""), row_factory=dict_row)

def creacionTablas():
  cursor = conn.cursor()
  cursor.execute('''
  CREATE TABLE IF NOT EXISTS canchas (
              id SERIAL PRIMARY KEY,
              nombre TEXT,
              disponible BOOLEAN DEFAULT TRUE)
  ''')

  cursor.execute('''
  CREATE TABLE IF NOT EXISTS reservas (
              id SERIAL PRIMARY KEY,
              nombre TEXT,
              hora_inicio TIME NOT NULL,
              hora_fin TIME NOT NULL,
              adelanto FLOAT,
              total FLOAT NOT NULL,
              cancha_id INT NOT NULL,
              FOREIGN KEY (cancha_id) REFERENCES canchas(id))
  ''')

  conn.commit()
  cursor.close()
  
creacionTablas()

@app.route('/canchas', methods=['POST', 'GET'])
def gestionCanchas() -> tuple[dict, int]:
    if request.method == 'POST':
        data = request.get_json()
        try:
            validador = CanchaSchema()
            dataValidada = validador.load(data)

            cursor = conn.cursor()
            cursor.execute('INSERT INTO canchas (nombre, disponible) VALUES (%s, %s) RETURNING *', (dataValidada.get('nombre'), dataValidada.get('disponible', True)))

            conn.commit()
            canchaCreada = cursor.fetchone()

            cursor.description

            columnas = []
            for column in cursor.description:
                columnas.append(column[0])

            cursor.close()

            resultado = validador.dump(canchaCreada)

            return {
                'message': 'Cancha creada exitosamente',
                'content': resultado
            }, 201 # Created
        
        except ValidationError as marshmallowError:
            return {
                'message': 'Error al validar la data',
                'errors': marshmallowError.args
            }, 400 # Bad Request
        
        def crearReserva():
          # Crear un ReservaSchema con las validaciones correspondientes
          # al recibir la canchaId validar que esta cancha exista, si no existe, retornar un mensaje de error que la cancha es invalida
          # Si todo esta bien, crear la reserva
          # {
          #    "nombre": "Eduardo",
          #    "horaInicio": "10:00",
          #    "horaFin": "12:00",
          #    "adelanto": 0.0,
          #    "total": 90.00,
          #    "canchaId": 1,
          # }
          pass

    @app.route('/reservas', methods=['POST'])
    def crearReserva() -> tuple[dict, int]:
      data = request.get_json()
    validador = ReservaSchema()

    try:
        dataValidada = validador.load(data)

        cursor = conn.cursor()

        # Verificar si la cancha existe
        cursor.execute('SELECT * FROM canchas WHERE id = %s', (dataValidada['canchaId'],))
        cancha = cursor.fetchone()

        if not cancha:
            cursor.close()
            return {
                'message': 'La cancha indicada no existe'
            }, 400  # Bad Request

        # Insertar la reserva
        cursor.execute('''
            INSERT INTO reservas (nombre, hora_inicio, hora_fin, adelanto, total, cancha_id)
            VALUES (%s, %s, %s, %s, %s, %s)
            RETURNING *
        ''', (
            dataValidada['nombre'],
            dataValidada['horaInicio'],
            dataValidada['horaFin'],
            dataValidada.get('adelanto', 0.0),
            dataValidada['total'],
            dataValidada['canchaId']
        ))

        conn.commit()
        reservaCreada = cursor.fetchone()
        cursor.close()

        resultado = validador.dump(reservaCreada)

        return {
            'message': 'Reserva creada exitosamente',
            'content': resultado
        }, 201  # Created

    except ValidationError as marshmallowError:
        return {
            'message': 'Error al validar la data',
            'errors': marshmallowError.messages
        }, 400

    else:
        cursor = conn.cursor()
        serializador = CanchaSchema()
        cursor.execute('SELECT * FROM canchas')
        canchas = cursor.fetchall()

        resultado = serializador.dump(canchas, many=True)

        return {
          'content': resultado
        }, 200 # OK

if __name__ == "__main__":
  app.run(debug=True)