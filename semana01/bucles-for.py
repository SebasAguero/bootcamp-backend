alumnos = ['Sebastian','Jose', 'Paolo', 'Eduardo','Keing','Luis']

# for > itera determinados pasos
# in en el bucle for sirve como asignacion
for nombre_alumno in alumnos:
    if nombre_alumno == 'Paolo':
        # si quiero saltarme una iteracion
        continue
    print(nombre_alumno)

# Se puede iterar el texto
texto = 'Hoy es fin de mes'
for letra in texto:
    print(letra)

numeros = [10, 40, 50, 60]

for numero in numeros:
    # pass indicar que aun no hay logica en este bloque de codigo
    # {}
    pass


# for tradicional
# desde el 0 hastsa menor que 4
for numero in range(4):
    print(numero)

# range(n) > tope, hasta que numero va a iterar
# range(n,m) > n numero_inicial
#              m tope 

for numero in range(1,7):
    print(numero)

# range(n,m,i) > n numero_inicial
#                m tope
#                p incrementador o decrementador
print('-----------')
for numero in range(5,10,3):
    print(numero)


# bandera: variable que sirve como incrementador para contar
veces_repetidas = 0
for numero in range(2,100,2):
    # modulo
    if numero % 3 == 0:
        # incrementando en uno la cantidad de el valor que tenia las veces_repetidas
        # veces_repetidas++
        veces_repetidas += 1
        # veces_repetidas = veces_repetidas + 1
        
        # decrementando
        # veces_repetidas -= 1
        # veces_repetidas = veces_repetidas - 1

print(veces_repetidas) # 0



# Usando el siguiente texto
texto = 'Hola, mi nombre es Eduardo y me gustaria aprender backend'
# necesito sber cuantas vocales hay en el texto y cuantos espacios tengo
contador_vocales = 0
contador_espacios = 0

for letra in texto:
    if letra.casefold() in ('a','e','i','o','u'):
        contador_vocales += 1
    if letra == ' ':
        contador_espacios += 1

print('Contador de espacios: ',contador_espacios)
print('Contador de vocales: ',contador_vocales)