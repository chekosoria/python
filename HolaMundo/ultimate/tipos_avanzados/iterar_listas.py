"""Iterar listas en Python"""
mascotas = ["Puka", "Coca", "Ninfa", "Pancho"]

# Itera la lista completa
for mascota in mascotas:
    print(mascota)


# Itera asignando un "id", la salida es una tupla
for mascota in enumerate(mascotas):
    print(mascota)
    # Se puede acceder a los valores en la tubla como
    # si fueran listas
    # print(mascota[0])

# Se puede asignar un nombre al índice
for indice, mascota in enumerate(mascotas):
    print(indice, mascota)
