# Tengo una tienda de ropa Eduardo's clothes
# Tengo ropa con las siguientes caracteristicas:
# Masculino en las tallas XL o L 
# Femenino con talla L o M

# Hacer un programa que recepcione el genero y la talla e indique si tiene o no tiene stock

# Solucion 1
tienda_ropa = {
  'masculino': ['l', 'xl'],
  'femenino': ['m', 'l']
}

genero = input('Ingrese el género: ').casefold()
talla = input('Ingrese la talla: ').casefold()


if talla in tienda_ropa[genero]:
    print('Sí hay stock')
else:
    print('No hay stock')


# Solucion 2
if genero == 'masculino' and talla == 'xl':
    print('Si hay stock')

elif genero == 'masculino' and talla == 'l':
    print('Si hay stock')

elif genero == 'femenino' and talla == 'l':
    print('Si hay stock')

elif genero == 'femenino' and talla == 'm':
    print('Si hay stock')

else:
    print('no hay stock')


# Solucion 3
if genero == 'masculino':
    if talla == 'xl' or talla == 'l':
        print('si hay stock')
    else:
        print('no hay stock')

elif genero == 'femenino':
    if talla == 'l' or talla == 'm':
        print('si hay stock')
    else:
        print('no hay stock')

else:
    print('genero no reconocido')


# Solucion 4
if genero == 'masculino' and talla in ('xl', 'l'):
    print('si hay stock')
elif genero =='femenino' and talla in ('l', 'm'):
    print('si hay stock')
else:
    print('no hay stock')