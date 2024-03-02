edad = 22

print(edad > 18 and edad < 30)
"""
El operador and evalua de izquierda a derecha por lo tanto si el resultado de la primera condición es False no continua con el resto
y da como resultado False
"""
print(edad > 18 or edad < 30)
"""
Para que el operador or regrese True basta que una de las condiciones sea True
"""
print(not(edad > 17))
"""
El operador not cambia el resultado de la condición evaluada dentro de los paréntesis
"""
