"""Manipular listas en Python"""

mascotas = ["Puka", "Coca", "Ninfa", "Pancho"]

print(mascotas[0])
mascotas[0] = "Pukahontas"
print(mascotas[0])
print(mascotas[0:3])
print(mascotas[:3])
print(mascotas[2:])
# Comienza a leer la lista desde el último elemento
print(mascotas[-1])
# Muestra un elemento si, uno no
# acepta agregar índice de inicio
print(mascotas[::2])
print(mascotas[1::2])

numeros = list(range(21))

print(numeros[1::2])
