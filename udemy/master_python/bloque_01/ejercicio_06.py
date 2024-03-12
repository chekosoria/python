"""
Ejercicio 06.
     - Mostrar todas las tablas de multiplicar del 1 al 10
       mostrando el título de la tabla y luego las operaciones
"""
for contador in range(1, 11):
    print(f"\n----- Mostrando la tabla del {contador} -----\n")
    for numero in range(1, 11):
        print(f"{contador} X {numero} = {contador * numero}")
