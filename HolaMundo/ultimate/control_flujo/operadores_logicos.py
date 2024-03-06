"""Operadores lógicos"""

EDAD = 22

print(30 < EDAD > 18)

# El operador and evalua de izquierda a derecha por
# lo tanto si el resultado de la primera condición es False no continua con el resto
# y da como resultado False

print(EDAD > 18 or EDAD < 30)

# Para que el operador or regrese True basta que una de las condiciones sea True
# print(not (EDAD > 17))
# El operador not cambia el resultado de la condición evaluada dentro de los paréntesis

# También se puede obviar la igualdad a true

GAS = True
ENCENDIDO = True

if GAS and ENCENDIDO:
    print("El auto puede avanzar")

# Con el operador OR funciona de la misma manera

DIA = False
NOCHE = True

if DIA or NOCHE:
    print("Es un buen momento para tomar café")
