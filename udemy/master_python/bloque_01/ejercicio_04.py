"""
Ejercicio 04.
     - Pedir dos números al usuario y hacer todas las operaciones
       básicas de una calculadora (suma, resta, multiplicación
       y división)
"""
print("----------------------------------------")
print("|---------- MINI CALCULADORA ----------|")
print("----------------------------------------")
print("Para suma ingrese ...................(s)")
print("Para resta ingrese ..................(r)")
print("Para multiplicación ingrese .........(m)")
print("Para división ingrese ...............(d)")
print("----------------------------------------")
opcion = input("Ingresa opción: ").lower()
n1 = int(input("Ingresa primer número: "))
n2 = int(input("Ingresa segundo número: "))

if opcion == "s":
    print(f"El resultado de la suma es: {n1 + n2}")
elif opcion == "r":
    print(f"El resultado de la resta es: {n1 - n2}")
elif opcion == "m":
    print(f"El resultado de la multiplicación es: {n1 * n2}")
elif opcion == "d":
    print(f"El resultado de la división es: {n1 / n2}")
else:
    print("Opción no soportada")
