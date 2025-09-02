edad = 26
# No tenemos llaves para definir bloques de codigo
# Tenemos IDENTACION (espaciado) para indicar que ese codigo estara dentro de un bloque
if edad > 18:
    print('Eres mayor de edad')
else:
    print('Eres menor de edad')

print('Finalizacion del if')

edad = 26
if edad > 18 and edad > 35:
    print('Puedes postular para la presidencia')
# Si queremos agregar una condicional intermedia antes que ingrese al else
elif edad > 18:
    print('Eres mayor de edad pero aun no puedes postular a la presidencia')
else:
    print('Eres menor de edad')


# Como saber si un numero es positivo o negativo o si es cero
numero = 0

if numero > 0:
    print('El numero es positivo')
elif numero < 0:
    print('El numero es negativo')
else:
    print('El numero es cero')

# Se puede ingresar valores por la terminal
numero_ingresado = input('Ingresa tu numero favorito:')

print(numero_ingresado)
print(type(numero_ingresado))

# Para convertir un tipo de dato a otro 
numero_ingresado_int = int(numero_ingresado)
print(type(numero_ingresado_int))

# > (Mayor), >= (Mayor o igual), < (Menor), <= (Menor o igual), == (igual que), != (diferente)

# Ingresando el pais indicar la nacionalidad
# Peru > Peruano
# Bolivia > Boliviano
# Holanda > Holandes
# Otro pais que no este registrado indicar que es Latinoamericano


# A parte de recibir el valor lo estamos convirtiendo a minusculas para que la busqueda sea exacta
# Concatenacion de metodos 
pais = input('Ingresa tu pais: ').casefold()

if pais == 'peru':
    print('Peruano')
elif pais == 'bolivia':
    print('Boliviano')
elif pais == 'holanda':
    print('Holandes')
else:
    print('Eres latinoamericano')