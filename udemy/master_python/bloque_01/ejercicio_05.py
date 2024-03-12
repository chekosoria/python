"""
Ejercicio 05.
     - Hacer un programa que muestre todos los números entre dos
       números que ingrese el usuario
"""
N1 = int(input("Ingrese primer número: "))
N2 = int(input("Ingrese segundo número: "))

for mostrar in range(N1, N2+1):
    print(f"- {mostrar}")
