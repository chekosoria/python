"""If ternario"""
EDAD = int(input("Ingresa tu edad: "))

# Se debe asignar una variable y dentro de ella se
# definiran las condiciones del if y el else
# variable = valor if condición else valor alternativo

MENSAJE = "Es mayor" if EDAD > 17 else "Es menor"

print(MENSAJE)
