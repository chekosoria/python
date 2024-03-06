"""Ciclo for"""
import random

NOMBRES = ["Homero", "Bart", "Lisa"]
EDAD = [41, 10, 9]

# En este caso, i se utiliza como contador y al utilizar enumerate, se obtiene
# tanto el índice como el elemento en cada iteración del bucle, permitiendo
# acceder a cada elemento del segundo arreglo utilizando i.

for i, nombre in enumerate(NOMBRES):
    print(f"{nombre} tiene {EDAD[i]} años")


BUSCAR = int(input("Ingresa número: "))

RANGO = random.randint(1, 100)

for numero in range(RANGO):
    if numero == BUSCAR:
        print("Encontrado", BUSCAR)
        break
else:
    print("No encontrado", BUSCAR)
