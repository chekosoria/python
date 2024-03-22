"""Modulo para manejar los menus disponibles en la aplicacion"""
import os


def clear_screen():
    """Función para limpiar la pantalla"""
    os.system('cls' if os.name == 'nt' else 'clear')


def mostrar_inicio():
    """Mostrar opciones de la aplicación"""
    print("--------------------------------")
    print("|         Bienvenidos          |")
    print("--------------------------------")
    print("|                              |")
    print("| Opciones disponibles:        |")
    print("|                              |")
    print("| Log in                    (1)|")
    print("| Log on                    (2)|")
    print("| Salir                     (3)|")
    print("|                              |")
    print("--------------------------------")


def inicio_notas():
    """Mostrar opciones de la aplicación"""
    print("--------------------------------")
    print("|            Notas             |")
    print("--------------------------------")
    print("|                              |")
    print("| Opciones disponibles:        |")
    print("|                              |")
    print("| Agregar                   (1)|")
    print("| Ver                       (2)|")
    print("| Eliminar                  (3)|")
    print("| Volver a menú principal   (4)|")
    print("|                              |")
    print("--------------------------------")


def inicio_borrar():
    """Mostrar opciones de la aplicación"""
    print("--------------------------------")
    print("|        Borrar notas          |")
    print("--------------------------------")
    print("|                              |")
    print("| Opciones disponibles:        |")
    print("|                              |")
    print("| Por ID de la nota         (1)|")
    print("| Por usuario               (2)|")
    print("| Volver a menú principal   (3)|")
    print("|                              |")
    print("--------------------------------")
