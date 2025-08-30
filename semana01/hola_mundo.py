saludo = 'Bienvenidos al curso de backend'
print(saludo)
saludo = 20
print(saludo)
print(type(saludo))

# se puede usar comillas simples o dobles mejor lo desee
# se debe usar comillas simples cuando  dentro del texto tengamos comillas dobles

# msi queremos tener un texto con salto de linea entonces usaremos la tripe comilla simple o triple comilla doble

dialogo = '''ahora, les contare un ejemplo de salto de linea
            esta es una nueva linea
            y esta es otra linea'''

print(dialogo)

curso, mes, dia, habilitado, nota = "backend", "agosto", 30, True, 14.5

print(curso)

# str | int | float | boolean

print(type(curso))
print(type(dia))
print(type(habilitado))
print(type(nota))