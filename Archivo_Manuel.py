# Una empresa vende hojas  con las condiciones siguientes:
# • Si el cliente es tipo 1 se le descuenta el 5%.
# • Si el cliente es tipo 2 se le descuenta el 8%.
# • Si el cliente es tipo 3 se le descuenta el 12%.
# • Si el cliente es tipo 4 se le descuenta el 15%.
# Cuando un cliente realiza una compra generan los datos siguientes
# • Nombre del cliente
# • Tipo de cliente (1,2,3,4)
# • cantidad de hojas compradas
# • Precio por hoja
# Elaborar un algoritmo que permita procesar varios clientes e imprima el reporte.

cantidad_cliente=0
venta_total=0
total_hojas_vendidad=0

while True:

    print("1.Comprar\n2.Reporte\n3.Salir")


    opc=int(input("Digite la opción "))
    match opc:
        case 1:
            nombre_cliente=input("Nombre del cliente: ")
            tipo_cliente=int(input("Digite el tipo de cleinte (1,2,3,4)"))#3
            cantidad_hojas=int(input("Cantidad de hojas: "))#1000

            PRECIO_HOJA=0.50
            #500
            precio_total=cantidad_hojas * PRECIO_HOJA

            if tipo_cliente ==1:
                descuento =precio_total *5/100
            elif tipo_cliente == 2:
                descuento = precio_total * 8/100
            elif tipo_cliente == 3:
                #60              500
                descuento = precio_total * 12/100
            elif tipo_cliente == 4:
                descuento = precio_total *15/100
            else:
                print("El tipo de cliente no existe")

            total_hojas_vendidad = total_hojas_vendidad + cantidad_hojas
            venta_total = venta_total + precio_total
            cantidad_cliente = cantidad_cliente + 1


            
            print("REPORTE DE VENTAS".center(30,"="))
            print("Cliente:        ",nombre_cliente)
            print("Cantidad hojas  ",cantidad_hojas)
            print("Tipo de cliente ",tipo_cliente)
            print(f"Descuento      ${descuento:,.1f}")
            print(f"Total          ${precio_total-descuento:,.1f}")
            print("Fin del reporte".center(30,"="))

            
  

        case 2:
            print("REPORTE TOTAL DE VENTAS".center(30,"="))
            print("Cantidad de aclientes ",cantidad_cliente)
            print("Total hojas vendidas  ",total_hojas_vendidad)
            print(f"Toal ventas          ${venta_total:,.1f}")
