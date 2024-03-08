"""Despuración de código"""


def largo(texto):
    """Función de prueba para mostrar el largo de una cadena"""
    resultado = 0
    for _ in texto:
        resultado += 1
    return resultado


print("Puka")

L = largo("Hola mundo")

print(L)
