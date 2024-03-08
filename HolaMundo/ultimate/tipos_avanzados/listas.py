"""Listas en Python"""

# Los elemetos de la lista van dentro de [] y se separan con ,
# los índices para acceder a los elementos comienzan en 0

# Lista de enteros

numeros = [1, 2, 3]

# Lista de caracteres

letras = ["a", "b", "c"]

# Lista de cadenas

palabras = ["hola", "mundo"]

# Lista de listas(matriz)

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Crea lista con N cantidad del mismo elemento

ceros = [0] * 10

# Crea lista concatenando dos o más listas

alfanumerico = numeros + letras

# Crea lista a partir de un rango, el primer argumento es el inicio
# y el segundo es el fin del rango

rango = list(range(1, 11))

# Lista a partir de un string

chars = list("Hola mundo")

print(numeros)
print(letras)
print(palabras)
print(matriz)
print(ceros)
print(alfanumerico)
print(rango)
print(chars)
