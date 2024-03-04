"""Cadenas en Python"""
NOMBRE_CURSO = "Ultimate Python"
DESCRIPCION_CURSO = """
Ultimate Python,
este curso contempla todos los detalles
que necesitas aprender para encontrar
un trabajo como programador
"""

print(NOMBRE_CURSO, DESCRIPCION_CURSO)

# La función len permite conocer la longitud de una cadena de
# caracteres y se debe mandar como argumento el nombre de la
# variable

print(len(NOMBRE_CURSO))

# Para mostrar un caracter determinado de la cadena dentro de
# los [] se debe pasar como argumento el índice que se desea
# mostrar tomando en cuenta que el conteo de índices SIEMPRE
# comienza desde 0

print(NOMBRE_CURSO[0])

# Para mostrar un rango de caracteres de la cadena dentro de
# los [] se debe pasar como argumento el índice inicial e índice
# final separados por :

print(NOMBRE_CURSO[1:3])

# Para mostrar un rango de caracteres de la cadena sin dar un índice
# final, dentro de los [] se debe pasar como argumento el índice
# inicial y : esto mostrará el resto de la cadena a partir del índice
# inicial que pasemos como argumento

print(NOMBRE_CURSO[5:])

# Para mostrar un rango de caracteres de la cadena sin dar un índice
# inicial, dentro de los [] se debe pasar como argumento los : seguidos
# del índice final esto mostrará desde el inicio de la cadena hasta
# índice final que pasemos como argumento

print(NOMBRE_CURSO[:8])

# Si no se pasa como argumento ninguno de los dos índices se mostrará
# la cadena completa

print(NOMBRE_CURSO[:])
