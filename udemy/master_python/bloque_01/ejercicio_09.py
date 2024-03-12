"""
Ejercicio 09.
     - Hacer un programa que pida números al usuario indefinidamente
       haste que ingrese el 111
"""
numero = int(input("Adivina el número: "))

while numero != 111:
    print("Incorrecto!!!")
    numero = int(input("Intente de nuevo: "))


print("Ha adivinado el número!!!")
