#  Escribe un programa que solicite al usuario su nombre y su
# edad. Posteriormente, debe imprimir un mensaje de bienvenida informando cuántos años cumplirá el
# usuario el próximo año.

# nombre=input("digite su nombre ")
# edad=int(input("digite su edad actual "))
# print("felicidades",nombre,"el proximo año cumpliras ",edad+1,"años")

# # Un comercio requiere calcular la factura de un cliente. Solicita
# el precio unitario de un producto y la cantidad comprada. Calcula el subtotal, aplica el IVA (19%) y
# muestra el subtotal, el impuesto y el total a pagar.

precio_producto=float(input("ingrese el precio del producto: "))
cantidad_producto=int(input("ingresa la cantidad de productos: "))
subtotal=precio_producto*cantidad_producto
iva=subtotal*0.19
total=subtotal+iva
print()
print("="*40)
print("total factura. \nsubtotal:",subtotal,"\niva : ",iva,"\n total ",total)
