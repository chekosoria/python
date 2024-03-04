"""Formato de cadenas"""
NOMBRE = "Sergio"
APELLIDO = "Soria"

# Para concatenar valores se usa el signo de +

NOMBRE_COMPLETO = NOMBRE + " " + APELLIDO

print(NOMBRE_COMPLETO)

# Una mejor manera de concatenar valores en cadenas es
# el uso del formateador de cadenas f en el que se pueden
# utilizar las variables directamente como si fueran parte
# de la cadena solo se deben escribir dentro de {}
# también es posible hacer funciones como {2 + 3}

FULL_NAME = f"{NOMBRE} {APELLIDO}"

print(FULL_NAME)
