"""Alcance de las funciones en Python"""

# Definición de variable global lo cual es una MALA practica

SALUDO = "Saludo global"

# Las variables saludo solo son accedidas por las
# funciones por lo que son distintas aunque se llaman igual


def saludar():
    """Saludo general"""
    saludo = "Hola mundo"
    print(saludo)


def saluda_user():
    """Saludo al usuario"""
    saludo = "Hola Cheko"
    print(saludo)


print(SALUDO)
saludar()
saluda_user()
