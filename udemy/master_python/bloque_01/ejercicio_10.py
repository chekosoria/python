"""
Ejercicio 10.
     - Hacer un programa que pida la calificación de 15 alumnos y
       muestre cuantos han aprobado y cuantos han reprobado.
"""
APROBADOS = 0
REPROBADOS = 0

contador = int(input("Cuántas calificaciones desea capturar: "))

for contador in range(1, contador+1):
    nota = float(input(f"Ingrese calificación del alumno {contador}: "))
    if nota >= 6:
        APROBADOS += 1
    else:
        REPROBADOS += 1

print(f"Aprobados  : {APROBADOS}")
print(f"Reprobados : {REPROBADOS}")
