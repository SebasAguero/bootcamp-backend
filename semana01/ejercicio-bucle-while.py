# Adivinar el numero a la maquina
# Ingresar un numero del 1 al 10 
# si el numero ingresado esta fuera de este rango volver a pedirlo
# Adivinaremos el numero que la maquina escogio, si el numero que ingresamos es mayor que el numero que la maquina penso entonces imprimir "El numero es menor" y volver a pedir un numero, caso contrario imprimir "El numero es mayor" y volver a pedir un numero y si es el numero indicar que es el numero y terminar el while con un break
import random
# genera un numero aleatorio entre esos parametros
numero_a_adivinar = random.randint(1,10)
print(numero_a_adivinar)

while True:
    intento = int(input("Ingrese un número del 1 al 10: "))

    if intento < 1 or intento > 10:
      print("El número debe estar entre 1 y 10")
      continue

    if intento > numero_a_adivinar:
        print("El número es menor")
    elif intento < numero_a_adivinar:
        print("El número es mayor")
    else:
        print("¡Adivinaste el número!")
        break