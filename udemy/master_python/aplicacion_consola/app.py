"""Aplicación para agregar y mostrar notas de usuario"""
from login import autenticar
from view_manager import mostrar_inicio
from view_manager import inicio_notas
from view_manager import clear_screen
from view_manager import inicio_borrar
from user_manager import add_usr
from user_manager import get_info
from note_manager import agregar_nota
from note_manager import consultar_nota
from note_manager import borrar_nota
from note_manager import borrar_notas

while True:
    mostrar_inicio()
    while True:
        try:
            opcion_inicial = int(input("Ingrese opción: "))
            break
        except ValueError:
            print("Error: Por favor, ingrese un número válido.")

    if opcion_inicial == 1:

        username = input("Ingrese su nombre de usuario: ")
        password = input("Ingrese su contraseña: ")

        if not autenticar(username, password):
            print("Usuario o contraseña incorrectos")
        else:
            print("Bienvenido", get_info(username))
            clear_screen()

            while True:
                inicio_notas()
                while True:
                    try:
                        opcion_notas = int(input("Ingrese opción: "))
                        break
                    except ValueError:
                        print("Error: Por favor, ingrese un número válido.")
                if opcion_notas == 1:
                    mensaje = input(
                        "Ingrese una nota de hasta 250 caracteres: ")
                    agregar_nota(username, mensaje)

                elif opcion_notas == 2:
                    consultar_nota(username)

                elif opcion_notas == 3:
                    while True:
                        inicio_borrar()
                        while True:
                            try:
                                opcion_borrar = int(input("Ingrese opción: "))
                                break
                            except ValueError:
                                print("Error: Por favor, ingrese un número válido.")
                        if opcion_borrar == 1:
                            id_nota = int(
                                input("Ingrese el ID de la nota que desea borrar: "))
                            borrar_nota(id_nota)

                        elif opcion_borrar == 2:
                            borrar_notas(username)

                        elif opcion_borrar == 3:
                            break

                elif opcion_notas == 4:
                    break

    elif opcion_inicial == 2:
        username = input("Ingrese su nombre de usuario: ")
        password = input("Ingrese su contraseña: ")
        nombre = input("Ingrese su nombre: ")
        apellido = input("Ingrese su apellido: ")
        email = input("Ingrese su email: ")

        add_usr(username, password, nombre, apellido, email)

    elif opcion_inicial == 3:
        break

    else:
        print("Error: Opción no válida. Por favor, ingrese una opción válida.")
