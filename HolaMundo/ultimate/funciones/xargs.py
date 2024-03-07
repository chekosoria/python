"""Xargs en Python"""

# El nombre del parámetro debe ser en plural, se agrega un *
# antes del nombre del parámetro.
# Se debe resolver iterando cada valor de los argumentos que pasen al
# llamar la función


def suma(*numeros):
    """Función para sumar N cantidad de números"""
    resultado = 0
    for numero in numeros:
        resultado += numero
    print(resultado)


suma(2, 5)
suma(2, 5, 10)
suma(2, 5, 10, 100)
