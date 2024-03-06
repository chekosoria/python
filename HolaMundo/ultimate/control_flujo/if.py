"""If"""
EDAD = int(input("Ingresa tu edad: "))

# La sintaxis debe ser if expresión a evaluar:
# el código a ejecutar debe comenzar con una sangría para que
# Python lo considere como parte del if

if EDAD > 30:
    print("Te va a aburrir la película")

# Elif permite agregar una condición extra a evular
# IMPORTANTE: Python comienza a evaluar desde if, si la
# condición se cumple no continua evaluando el resto de
# la expresión

elif EDAD > 17:
    print("Puedes ver la película")

# Else permite agregar una salida al programa si las conficiones
# a evaluar no se cumplen
# Else no es obligatorio

else:
    print("No puedes entrar a ver la película")

print("Listo")
