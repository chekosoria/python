"""
- La función input() siempre tiene como tipo de dato por default str
- Para convertir a cadena se usa str()
- Para convertir a booleano se usa bool()
  NOTA: Los unicos valores que evaluan en False son:
    a. False
    b. 0 (número cero)
    c. "" (cadena vacía)
    d. None 
"""
# Se crea variable y se asigna su valor con pase a lo que el usuario ingrese

resultado = input("Ingresa tu edad: ")

# Se imprime la variable

print(resultado)

# Se immprime el tipo de dato de la variable

print(type(resultado))

# Se crea nueva variable y se le asigna el valor de la primera variable convertida a tipo entero

numero = int(resultado)

# Se imprime la nueva variable + 2

print(numero + 2)

# Se crea variable y se asigna su valor con pase a lo que el usuario ingrese

calificacion = input("Ingresa una calificacion: ")

# Se imprime la variable

print(calificacion)

# Se immprime el tipo de dato de la variable

print(type(calificacion))

# Se crea nueva variable y se le asigna el valor de la primera variable convertida
# a tipo decimal (float)

nota = float(calificacion)

# Se imprime la nueva variable + 2

print(nota + .5)
