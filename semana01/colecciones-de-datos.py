#variables que pueden almacenar diferentes informacion

numeros_tel = ['104','105','999444555','123']


#en la colecciones de datos se pueden agregar diferentes tipos de datos dentro de sus elementos

numeros_tel.append(False)
numeros_tel.append(10.5)

print(numeros_tel)
print(numeros_tel[0])

#tambien se puede obtener un subconjunto de elementos de la lista
print(numeros_tel[1:3])
#todos los elementos desde la posicion 2
print(numeros_tel[2:])
#todos los elementos hasta la posicion <2
print(numeros_tel[:2])

#para obtener el ultimo elemento usamos valores negativos y asi como se invierte la lista
print(numeros_tel[-1])



#formas de eliminar elementos de una lista

#con el metodo POP retiramos el elemento de la lista y lo podemos almacenar en otra variable

valor_eliminado = numeros_tel.pop(0)
print(valor_eliminado)
print(numeros_tel)

#del > sirve para eliminar varibles (liberar espacio de memoria) y tambien se puede eliminar elementos de una lista

del numeros_tel[1]
print(numeros_tel)

#si se quiere limpiar completamente la lista

numeros_tel.clear()
print(numeros_tel)

ejercicio_1 = [1, 'Eduardo','de Rivero',False, 32, 20.5, [4,8,12]]

#como hago para obtener a 'de Rivero'

print(ejercicio_1[2])

#como hago para obtener desde eduardo hasta 32

print(ejercicio_1[1:5])

#como hago para obtener la penultima posicion 20.5

print(ejercicio_1[-2])

#como hago para obtener el valor 8

print(ejercicio_1[6][1])


data = ('Roxana', 'Pedro', [1,2,6,['Juan', 'Aristoteles']])
print(data[2][3][1])

persona = {
  'nombre': 'Carlos',
  'ciudad': 'Arequipa',
  'estado': 'Peruano',
  'nacionalidad': 'Peruano',
  'direccion': {
    'calle': 'Los Girasoles',
    ' numero':180,
    'manzana':3,
    'lote': None
  },
  'hobbies': ['Programar', 'Estudiar', 'Montar Bici']
}
print(persona['nombre'])

#Agregar elementos
persona['idiomas'] = ('Español', 'Ingles', 'Quechua')

#Editar un elemento
persona['estado'] = 'Soltero'

#Eliminar un elemento
persona.pop('nacionalidad')
del persona['estado']

print(persona)

#Llaves del diccionario
print(persona.keys())
print(persona.values())

#Obtener la calle
print(persona['direccion']['calle'])

#Obtener los dos últimos hobbies
print(persona['hobbies'][-2:])