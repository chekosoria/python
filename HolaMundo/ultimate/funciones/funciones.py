"""Funciones en Python"""

# La sintaxis para definir funciones es palabra reservada def
# seguida del nombre de la función y ()
# dentro de los () se definen los parámetros de la función
# si queremos agregar un valor por default a un parámetro
# colocamos un = después del nombre del parámetro seguido del valor


def hola(nombre, apellido="Thompson"):
    """Función para mostrar saludo por consola"""
    print(f"Hola mundo! \nMi nombre es {nombre} {apellido}")


# Cuando la función se manda llamar dentro de los ()
# se pasan los argumentos

hola("Homero")
hola("Bart", "Simpson")
hola("Lisa", "Simpson")

# Si requiero llamar la función pero no recuerdo el órden
# de los argumentos puedo nombrarlos y Python interpretará el dato
# y regresará el valor esperado

hola(apellido="Flanders", nombre="Ned")
