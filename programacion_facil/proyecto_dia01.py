"""
Proyecto día 1. Construir un programa que haga lo siguiente:
- Frase de saludo inicial
- Entrada del usuario preguntando el nombre
- Entrada del usuario preguntado la edad
- Entrada del usuario preguntando el páis de nacimiento
- Comentarios en cada sección del código
- Se deben tomar los datos ingresados por el usuario e imprimirlos en una frase final
- Se deben usar saltos de línea en el código para mejorar la presentación
"""
# Variable para almacenar saludo inicial
SALUDO = """*** Bienvenido al proyecto del día 1 ***\n\n
A continuación le pediremos algunos datos para después mostrarlos en consola
"""
print(SALUDO)

# Variable para almacenar el nombre ingresado por el usuario
nombre = input("Ingresa tu nombre: \n")
# Variable para almacenar la edad del usuario
edad = input("Ingrese su edad: \n")
# Variable para almacenar el país de origen del usuario
pais = input("Ingresa tu pais de origen: \n")
cadena_final = f"""Hola {nombre} de {
    edad} años, eres de {pais}\ny esta es la 1ra practica del curso de Python"""

print(cadena_final)


multiplicacion = 7.5678 * 6.943534

print(multiplicacion, 2)
