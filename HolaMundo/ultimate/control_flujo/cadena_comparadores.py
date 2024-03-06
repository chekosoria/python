"""Cadena comparadores"""

EDAD = int(input("Ingresa edad: "))

# El operador and evalua de izquierda a derecha por
# lo tanto si el resultado de la primera condición es False no continua con el resto
# y da como resultado False

if 18 <= EDAD <= 65:
    print("Puede entrar")
else:
    print("No puede entrar")
