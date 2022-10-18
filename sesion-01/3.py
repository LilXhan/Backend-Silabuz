"""
Problema3
Ingresar desde teclado un consumo. La tienda tiene descuento de 10% si el consumo es mayor a 100, pero si es consumo
 es mayor a 300 y es fin de semana el descuesto es de 20%
"""

consumo = int(input("Ingrese el consumo total:\n"))
day = int(input("Ingrese el número del dia de la semana:\n"))

while consumo <= 0:
    consumo = int(input("El consumo no puede ser menor que 0, ingrese un número correcto."))
while day < 0 and day > 7:
    day = int(input("Ingrese un numero de dia correcto."))


if consumo >= 100 and consumo <= 300:
    print("Su descuento es de: ", consumo * (10/100))

elif consumo >= 100 and consumo >= 300 and day in (5, 6, 7):
    print("Su descuento es de: ", consumo * (20/100))

else:
    print("No tiene descuento.")