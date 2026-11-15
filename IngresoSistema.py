# -*- coding: utf-8 -*-
# Fecha: Nov 13/26
# Autor: Cabelrod
# Algoritmos secuenciales con ciclos
''' Enunciado: Diseñe un algoritmo que permita al usuario autenticarse en el sistema utilizando el
nombre de usuario "pepe" y la clave "123".
El programa debe solicitar al usuario que ingrese su nombre y contraseña. Si alguno de
los datos es incorrecto, se le permitirá intentarlo nuevamente, mostrando el número de
intentos realizados.
Después de tres intentos fallidos, el sistema debe mostrar el mensaje: "Usuario
bloqueado".
Si el usuario ingresa correctamente sus credenciales antes de alcanzar el límite de
intentos, se mostrará un mensaje de bienvenida y se permitirá el acceso al sistema.'''

conta = 1
x=True # Se controla mensaje fallido
clave = 0
intento = 0
print()
print("\033[H\033[J", end="") # borrar la terminal
print('\n ******* SISTEMA BANK_CITY  ******* ') 
while conta <= 3 :

    usuario=(input(" --- Ingrese el nombre del Usuario ---> ")).lower()
    clave=int(input(" --- Digite la clave ---> "))
    
    if usuario == "pepe":
        if clave == 123:
            print(" ============================================================")
            print(f" --- Bienvenido al sistema usuario: {usuario} -------- ")
            x=False
            conta = 10
    
    if conta == 3:
        print(" ============================================================")
        print(" --- Usuario bloqueado por tres intentos fallidos -------- ")
        print(" --- Comuniquese con la administración -------- ")
        print(" ============================================================")
    else:
        if x == True:
            print(" ============================================================")
            print(" --- Datos errados -------- ")
            print(f" --- Lleva {conta} intentos de tres -------- ")
            print(" ============================================================")

    conta=conta+1        


print("\n --- fin proceso ---")
print()
#===============================================================================

'''Generar una temperatura inicial aleatoria entre 33 °C y 45 °C.
Mostrar en pantalla la temperatura inicial.
Mientras la temperatura sea mayor o igual a 34 °C, el programa debe:
Guardar la temperatura anterior.
Generar una nueva temperatura aleatoria entre 33 °C y 45 °C.
Comparar la temperatura nueva con la anterior y conservar el valor mayor en una variable.
Mostrar la temperatura actual.
Esperar 3 segundos antes de realizar una nueva lectura.
El proceso debe repetirse hasta que la temperatura sea inferior a 34 °C.'''

import random
import time

print()
print("¬")

time.sleep(3)
# 36
tem_inicial = random.uniform(33.5,45)
print(f"{tem_inicial:.1f}°C")
#          33
while tem_inicial >= 34:
#       38
    tem_nueva= tem_inicial
    #33
    tem_actual=random.uniform(33,45)
    #     33          38
    if tem_actual > tem_nueva:
        # 38
        tem_nueva=tem_actual
#                                         33
    print(f"Temperatura actual--------{tem_actual:.1f}°C")
    #33
    tem_inicial=tem_actual
    time.sleep(3)

#****************************************************************************
#Hacer una algoritmo que le pida una tabla al usuario
#El programa mostrara una multiplicación aleatoria y el ussuari deberá escribir 
#el resultado y tratar de repsponder en 10 segundo la mayor cantidad de multplicaciones.
#Generer una cunta regresiva y al final mostrar cuantos resultado acerto

import random
import time

print("Juego de Tablas contra reloj")
#8
tabla=int(input("¿Qué #_tabla quieres practicar? "))
print("Tines 10 segundos....")

cuenta = 3
#       3
while cuenta > 0:
    print(cuenta)
    time.sleep(2)
    cuenta =cuenta - 1
conrrectas =0
print("\nYA\n")



inicio = time.time()#9:30:12
#       9:30:20   9:30:12=8 
while time.time() - inicio <= 10:
#     7
    multi=random.randint(1,10)
    # 56                        8          7
    respuesta = int(input(f"{tabla} x {multi} = "))
#     #   56             56 
    if respuesta == tabla*multi:
        #  1             0 +1
        conrrectas = conrrectas + 1
        print("Muy Bien")
    else:
        print("✖️ Error ")
        print("El resultado correcto es ",tabla*multi)

    time.sleep(0.1)


print("Se terminó el tiempo")
print("Acertate ",conrrectas)

#***********************************************************************
import random
import time
opc="si"
while opc=="si":
    print("Juego de Tablas contra reloj")
    #8
    #tabla=int(input("¿Qué tabla quieres practicar? "))
    print("Tines 10 segundos....")

    cuenta = 3
    #       3
    while cuenta > 0:
        print(cuenta)
        time.sleep(1)
        cuenta =cuenta - 1


    correctas =0
    print("\nYA\n")
    inicio = time.time()#9:30:12
    #       9:30:20   9:30:12=8 
    while time.time() - inicio <= 10:
        tabla=random.randint(1,20)
        multi=random.randint(1,10)
        # 56                        8          7
        respuesta = int(input(f"{tabla} x {multi} = "))
    #     #   56             56 
        if respuesta == tabla*multi:
            #  1             0 +1
            correctas = correctas + 1
            print("Muy Bien")
        else:
            print("✖️ Error ")
            print("El resultado correcto es ",tabla*multi)

        time.sleep(0.1)


    print("Se terminó el tiempo")
    print("Acertate ",correctas)

    opc=input("Digite 'si', en caso de quere ejecutar nuevamente el ejercicio de lo contrario digite no ")

    