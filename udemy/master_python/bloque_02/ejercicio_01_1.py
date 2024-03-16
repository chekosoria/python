"""
Ejercicio 01.1
    Hacer un programa que tenga una lista de números enteros y haga lo siguiente:
    - Creando un función recorrer la lista y mostrarla (retornando un str)
    - Ordenarla y mostrarla
    - Mostrar su longitud
    - Buscar un elemento (ingresado por el usuario)
"""


def recorrer(lista):
    """Función para recorrer y retornar elmentos de una lista"""
    for elemento in lista:
        print(elemento)


def convertir(lista):
    """Función para convertir una lista de enteros a str"""
    convertido = str(lista)
    return convertido


def ordenar(lista):
    """Función para ordenar y mostrar elementos de una lista"""
    ordenada = sorted(lista)
    return ordenada


def get_longitud(lista):
    """Función para obtener la longitud de una lista"""
    longitud = len(lista)
    return longitud


def get_index(lista, num):
    """Función para obtener el índice de un numero consultado por el usuario"""
    indice = lista.index(num)
    return indice


def get_value(lista, num):
    """Fución para obtener un valor basado en el índice ingresado por el usuario"""
    valor = lista[num]
    return valor


x = int(input("Ingresa un valor a buscar: "))
y = int(input("Ingrese un índice a buscar: "))

listado = [1, 2, 3, 12, 15, 96, 7, 8]

recorrer(listado)
print(convertir(listado))
print(ordenar(listado))
print(f"La longitud de la cadena es de {get_longitud(listado)}")
print(get_index(listado, x))
print(get_value(listado, y))
