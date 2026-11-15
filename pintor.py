#Mostrar números pares del 1 al 20 Escriba un algoritmo que muestre todos los números pares entre 1 y 20.
# Mostrar números pares del 1 al 20.

print("========== NÚMEROS PARES DEL 1 AL 20 ==========")

numero = 1

while numero <= 20:

    if numero % 2 == 0:
        print(numero)

    numero = numero + 1

#Mostrar números impares del 1 al 15 Escriba un algoritmo que muestre todos los números impares entre 1 y 15.

print("========== NÚMEROS IMPARES DEL 1 AL 15 ==========")

numero = 1
while numero <= 15:

    if numero % 2 != 0:
        print(numero)

    numero = numero + 1


multiplicador = int(input("Ingrese el multiplicador: "))
contador = 1

while contador <= 10:

    resultado = multiplicador * contador
    print(multiplicador,"x",contador,"=",resultado)
    
    contador = contador + 1

#pedir un número al usuraio y generar un número aleatorio, este será el número secreto
#si  este número es igual al que digito el usuario, saldra un mensaje, Ganaste de lo contrario el mensaje sera, "Perdiste". El usuario tendra 3 intentos de adivinar el número

import random
numero_secreto = random.randint(1, 10)

intentos = 3
while intentos > 0:
    numero_usuario = int(input("Adivina el número secreto (1-10): "))
    if numero_usuario == numero_secreto:
        print("¡Ganaste!")
        break
    else:
        print("Perdiste.")
        intentos = intentos - 1
print("El número secreto era:", numero_secreto)

















