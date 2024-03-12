"""
Ejercicio 08.
     - Hacer un programa que muestre cuanto es el X% de N
       solicitando N y X al usuario
"""
cantidad = int(input("Ingrese un número: "))
porcentaje = int(input("Ingrese el porcentaje a aplicar: "))
resultado = (cantidad * porcentaje) / 100

print(f"El {porcentaje}% de {cantidad} es {resultado}")
