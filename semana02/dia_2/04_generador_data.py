from faker import Faker
from datetime import date
# Creamos una instancia de nuestra clase
# instancia: copia de toda la configuracion de la clase que va a ser almacenada en la variable
creador = Faker()
def generar_data_profesores(cantidad):
    texto = 'INSERT INTO profesores (nombre, apellidos, correo, correo_institucional, activo, fecha_contratacion) VALUES '

    for numero in range(cantidad):
        nombre = creador.first_name()
        apellidos = creador.last_name()
        correo = creador.email(True)
        correo_institucional = creador.email(True,'codigo.edu.pe')
        activo = creador.boolean()
        fecha_contratacion = creador.date_between(start_date=date(2022,1,15),end_date=date(2025,8,1))

        data = "('{}','{}','{}','{}',{},'{}'),".format(nombre,
                                                    apellidos,
                                                    correo,
                                                    correo_institucional,
                                                    activo,
                                                    fecha_contratacion)

        # Al ser string no se hara sumatoria sino se realizara una concatenacion
        texto += data
        # En el ultimo registro en vez de colocar una coma se coloque un `;`

    resultado = texto.rsplit(',',1)[0] + ';'

    print(resultado)

    # agregando al comando `> NOMBRE_ARCHIVO.EXT` en vez de mostrarlo en la terminal las impresiones de pantalla lo guardara en ese archivo definido en la terminal

def generar_data_direcciones(cantidad):
    texto = 'INSERT INTO direcciones (calle, numero, referencia, distrito, provincia, profesor_id) VALUES '

    distritos_disponibles = ['Arequipa','Lima','Jesus Maria', 'Cuzco', 'Tacna', 'Ite', 'Ilo', 'Trujillo']
    provincias_disponibles = ['Aija', 'Antonio Raimondi', 'Asunción', 'Bolognesi', 'Carhuaz', 'Casma', 'Corongo', 'Huarmey', 'Huaylas', 'Pallasca', 'Pomabamba', 'Recuay', 'Santa', 'Sihuas', 'Yungay','Cajamarca', 'Cajabamba', 'Celendín', 'Chota', 'Contumazá', 'Cutervo', 'Hualgayoc', 'Jaén', 'San Ignacio', 'San Marcos', 'San Miguel', 'San Pablo', 'Santa Cruz']
    for numero in range(cantidad):
        calle = creador.street_name()
        numero = creador.building_number()
        referencia = creador.word()
        distrito = creador.random_element(distritos_disponibles)
        provincia = creador.random_element(provincias_disponibles)
        profesor_id = creador.random_int(1,103)

        data = "('{}','{}','{}','{}','{}', {}),".format(calle,
                                                        numero,
                                                        referencia,
                                                        distrito,
                                                        provincia,
                                                        profesor_id)
        texto += data
    
    resultado = texto.rsplit(',',1)[0] + ';'

    print(resultado)
# Para leer este archivo en la terminal
# MAC | Powershell | GitBash : cat
# CMD (windows): type


generar_data_direcciones(200)