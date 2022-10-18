month = int(input("Ingrese el digito de un mes:\n"))


while month < 0 or month > 12:
    month = int(input("Ingrese el número de un mes entre 1 y 12.\n"))

lista = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Setiembre", "Octubre", "Noviembre", "Diciembre"]

contador = 0

while contador <= 12:
    if contador == month - 1:
        print("El mes es: ", lista[contador])
    contador += 1
