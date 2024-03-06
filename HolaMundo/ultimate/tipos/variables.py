"""Variables en Python"""
# Los nombres de las variables no pueden comenzar con un número
# Si se utiliza Pylance se deberá nombrar a las constantes con mayúscula
# siguiendo snake_case

# Variables de tipo cadena

NOMBRE_CURSO = "Ultimate Python"
VARIABLE = "Hola mundo"

print(NOMBRE_CURSO)
print(VARIABLE)

# Variable de tipo entero

NUMERO = 41

print(NUMERO)

# Variable de tipo decimal

DECIMAL = 10.5

print(DECIMAL)

# Variables de tipo booleano

VERDADERO = True
FALSO = False

print(VERDADERO)
print(FALSO)

# También es posible definir el tipo de la variable, la sintaxis
# para hacerlo es nombre_variable: tipo y valor
# para mejor lectura de números grandes se puede usar _ cada 3 dígitos

N: int = 1_000_000

print(N)

# Para usar separadores al imprimir números se puede usar f"{nombre_variable:separador}"

print(f"{N:,}")
