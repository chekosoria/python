"""Cadenas en Python"""

# Definición de variable tipo cadena

TEXTO = "Hola Mundo"

# Imprimir el texto en mayúsculas

print(TEXTO.upper())

# Imprimir el texto en minúsculas

print(TEXTO.lower())

# Busca el índice del caracter deseado

print(TEXTO.find("M"))

# Reemplaza la cadena original (temporalmente)

print(TEXTO.replace("Hola Mundo", "Hello World"))

# Asigna a una variable el reemplazo de la cadena original

NUEVOTEXTO = TEXTO.replace("Hola Mundo", "Hello World")

# Imprime las 2 variables

print(TEXTO, NUEVOTEXTO)

# Indica si la cadena buscada se encuentra en la variable

print("Mundo" in TEXTO)
