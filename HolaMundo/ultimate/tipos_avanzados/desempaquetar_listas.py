"""Desempaquetar listas en Python"""
numero = [1, 2, 3]

primero, segundo, tercero = numero

print(primero, segundo, tercero)

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

primero, *otros, penu, ultimo = numeros

print(primero, otros, penu, ultimo)


calificaciones = [5, 6, 7, 8, 9, 10]

a, *o, y, z = calificaciones

print(a, o, y, z)
