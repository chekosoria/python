"""
Ejercicio 02.
     - Escribir un script que muestre en pantalla todos los
       números pares del 1 al 120
"""
print("----- Números pares -----")

for par in range(1, 121):
    if par % 2 == 0:
        print(f"- {par}")
