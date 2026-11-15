# #Desarrolle un programa en python que simule el funcionamiento básico de un cajero automático. El sistema debe solicitar al usuario iniciar sesión antes de permitir cualquier operación. Para esto, se debe validar un usuario y una contraseña previamente definidos en el sistema.
# El programa debe ejecutarse de manera continua utilizando un ciclo while, permitiendo múltiples intentos de inicio de sesión hasta que las credenciales sean correctas.
# Una vez el usuario haya iniciado sesión correctamente, el sistema debe mostrar un menú con las siguientes opciones:
# 1. Consultar saldo
# 2. Consignar dinero
# 3. Retirar dinero
# 4. Salir
# El usuario podrá seleccionar una opción ingresando el número correspondiente. El sistema debe validar que la opción ingresada sea correcta.
# Para la opción de consignar dinero, el programa debe solicitar el valor a consignar y sumarlo al saldo actual.
# Para la opción de retirar dinero, el programa debe solicitar el valor a retirar y verificar que el saldo sea suficiente antes de realizar la operación. Si no hay fondos suficientes, se debe mostrar un mensaje indicando la situación.
# El sistema debe permitir realizar múltiples operaciones hasta que el usuario seleccione la opción de salir.
# ⚠️ Condiciones adicionales:
#  El usuario tiene máximo 3 intentos para iniciar sesión. Si falla, el sistema debe bloquear el acceso.

usuario_correcto = "Nur"
clave_correcta = "4567"  
saldo_actual = 1000  
intentos = 0

while intentos < 3:
    usuario_ingresado = input("Ingrese su nombre de usuario: ").lower()
    
    if usuario_ingresado == usuario_correcto:
        intentos = 0
        while intentos < 3:
            clave_ingresada = input("Ingrese su contraseña: ")

            if clave_ingresada == clave_correcta:
                print("¡Bienvenido al sistema!")

                while True:

                    print("1.Consultar_Saldo\n2.Consignar_Dinero\n3.Retirar_Dinero\n4.Salir")

                    opc=int(input("Digite la opción: "))

                
                    match opc:
                        case 1:
                            print(f"Su saldo es de: {saldo_actual:,.0f} pesos")
                        case 2:

                            valor_consignar = float(input("Ingrese el valor a consignar: "))

                            if valor_consignar <= 0:
                                print("El valor a consignar debe ser mayor que cero.")
                            else:
                                saldo_actual = saldo_actual + valor_consignar
                                print(f"Consignación exitosa. Su nuevo saldo es: {saldo_actual:,.0f} pesos")

                        case 3:
                            valor_retirar = float(input("Ingrese el valor a retirar: "))

                            if valor_retirar <= 0:
                                print("El valor a retirar debe ser mayor que cero.")

                            elif valor_retirar > saldo_actual:
                                print("Saldo insuficiente para realizar el retiro.")

                            else:
                                saldo_actual = saldo_actual - valor_retirar
                                print(f"Retiro exitoso. Su nuevo saldo es: {saldo_actual:,.0f} pesos")                          
                            
                        case 4:
                            print("Saliendo del sistema...")
                            break
                        case _:
                            print("Opción no válida. Por favor, seleccione una opción válida.")
                break
            else:
                intentos = intentos + 1
                print(f"Clave incorrecta. Intento {intentos} de 3.")
        break
    else:
        intentos =intentos + 1
        print(f"Usuario incorrecto. Intento {intentos} de 3.")

if intentos == 3:
    print("Usuario bloqueado.")
    print("Fin del programa.")

