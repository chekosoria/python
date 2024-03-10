"""Operador para desempaquetar en Python"""
lista = [1, 2, 3, 4]

print(lista)

print(1, 2, 3, 4)

# Para desempaca *variable
# aplica para cualquier iterable i.e. lista, string, etc.

print(*lista)


# Podriamos desempaquetar una lista y pasarla como argumentos
# de una función como sigue:

def n(n1, n2, n3, n4):
    """Función simple para calcula factorial del 4"""
    factorial = n1 * n2*n3*n4
    return factorial


print(f"4! = {n(*lista)}")

# Se puede concatenar un par de listas desempaquetandolas

lista2 = [5, 6]

combinada = [*lista, *lista2]

print(*combinada)

# También se pueden concatenar diccionarios desempaquetandolos

punto1 = {"x": 19}
punto2 = {"y": 15}

coordenada = {**punto1, **punto2}

print(coordenada)
