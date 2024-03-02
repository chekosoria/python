# Se crea variable y se asigna su valor con pase a lo que el usuario ingrese
calificacion = input("Ingrese calificacion del alumno: ")
# Se convierte la entra de usuario a decimales
nota = float(calificacion)

# Se evalua si se cumple la condición
if nota >= 9.5:
    print("Aprobado con honores")
# Si la primera condición no se cumple se evalua esta condición
elif nota >= 7.0:
    print("Aprobado con buena nota")
# Si la primera y segunda condiciones no se cumplen se evalua esta condición
elif nota >= 6.0:
    print("Apenas aprobado")
# Si ninguna de las condiciones se cumple se realiza esta acción
else:
    print("Reprobado")