value_one = int(input("Ingrese el primer valor:\n"))
value_two = int(input("Ingrese el segundo valor:\n"))

opcion = input("Ingrese la opcion que desea ejecutar:\n"
        "A. Sumar\n"
        "B. Restar\n"
        "C. Multiplicar\n"
        "D. Dividir\n")
    
while opcion not in ("A", "B", "C", "D"):
    opcion = input("Ingrese una opcion correcta.\n")

if opcion == "A":
    print("El resultado es: ", value_one + value_two)
elif opcion == "B":
    print("El resultado es: ", value_one - value_two)
elif opcion == "C":
    print("El resultado es: ", value_one * value_two)
else:
    print("El resultado es: ", value_one / value_two)
