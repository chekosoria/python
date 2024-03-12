"""
Ejercicio 07.
     - Hacer un programa que muestre todos los números impares entre
       dos números que decida el usuario.
"""
n1 = int(input("Ingrese primer número: "))
n2 = int(input("Ingrese segundo número: "))

for impar in range(n1, n2+1):
    if impar % 2 != 0:
        print(f"- {impar}")
