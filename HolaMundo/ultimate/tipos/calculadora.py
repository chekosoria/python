"""Calculadora"""
n1 = int(input("Ingresa primer número  : "))
n2 = int(input("Ingresa segundo número : "))

suma = n1 + n2
resta = n1 - n2
multi = n1 * n2
div = n1 / n2

MENSAJE = f"""
Para los números {n1} y {n2}, los resultados son:
suma = {suma}
resta = {resta}
multiplicación = {multi}
división = {div}
"""

print(MENSAJE)
