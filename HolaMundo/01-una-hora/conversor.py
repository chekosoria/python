"""Conversor de grados"""
# Se asigna la variable de temperatura y se le da valor con base a lo ingresado
# por el usuario convirtiendo directamente el dato a float

temperatura = float(input("Ingrese temperatura: "))

# Se muestran las instricciones

print("Ingrese C para convertir Celsius a Fahrenheit")
print("o Ingrese F para convertir Fahrenheit a Celsius")

# Se asigna la variable escala y se le da valor con base a lo ingresado por
# el usuario convirtiendo el dato ingresa en minúscula

escala = input("Ingrese seleccion: ").lower()

# Se crea variable para almacenar la temperatura convertida y se inicializa con valor 0.0

T = 0.0

# Se evalua si la selección de escala es igual a "c"

if escala == "c":
    # Se convierte la temperatura ingresada

    T = (temperatura - 32) * (5/9)

    # Se crea variable para mostrar la temperatura convertida y se le asigna el valor convertido
    # a str de la variable t

    NUEVA = str(T)
    # Se muestra el resultado de la conversión
    print("La temperatura es de " + NUEVA + " grados Celsius")
# Se evalua si la selección de escala es igual a "f"
elif escala == "f":
    # Se convierte la temperatura ingresada
    T = (temperatura * (9/5)) + 32

    # Se crea variable para mostrar la temperatura convertida y se le asigna el valor convertido
    # a str de la variable t

    NUEVA = str(T)

    # Se muestra el resultado de la conversión

    print("La temperatura es de " + NUEVA + " grados Fahrenheit")

# Si la selección de escala no es igual a "c" o "f" se muestra mensaje de excepción

else:
    print("Opción no soportada")
