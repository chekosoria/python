"""Ejercicio 1 . Clases"""
# Crear una clase Estudiate
# Atributos Nombre, edad, grado
# Métodos estudiar() "El estudiante (nombre) está estudiando"
# Crear un objeto estudiante y usar el método estudiar()
# Se debe interactuar con el usuario y este debe brindar los atributos
# Al escribir "estudiar" utilizar el método estudiar() (no case sensitive)


class Estudiante:
    """Clase para crear estudiantes"""

    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado

    def estudiar(self):
        """Función para indicar que está estudiando"""
        print(f"El estudiante {self.nombre} está estudiando")


print("Hola, ingresa los siguientes datos: ")
name = input("Nombre: ")
age = int(input("Edad: "))
grade = int(input("Grado: "))

accion = input(f"Qué hace {name}? ").lower()


if accion == "estudiar":
    Estudiante1 = Estudiante(name, age, grade)
    Estudiante1.estudiar()
else:
    print(f"{name} debería estar estudiando")
