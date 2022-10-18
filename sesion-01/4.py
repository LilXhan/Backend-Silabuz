nota = int(input("Ingrese la nota:\n"))

a = 0

a = ("Aprobado" if nota > 10 else "Deficiente") if nota < 15 else ("Excelente" if nota > 18 else "Bueno")
print(a)