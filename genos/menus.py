"""Creación de Menús"""
import tkinter as tk
from tkinter import messagebox


def crear_menus(app):
    """Función para crear menús"""
    menu_bar = tk.Menu(app)
    app.config(menu=menu_bar)

    # Menú de archivo

    app_menu = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Archivo", menu=app_menu)
    app_menu.add_command(
        label="Inicio", command=lambda: app.mostrar_frame("Home"))

    # Menú de aplicaciones

    app_menu = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Aplicaciones", menu=app_menu)
    app_menu.add_command(
        label="Agregar Endpoint", command=lambda: app.mostrar_frame("AddEndPoint"))
    app_menu.add_command(
        label="Editar Endpoint", command=lambda: app.mostrar_frame("EditEndPoint"))
    app_menu.add_command(
        label="Probar Endpoint", command=lambda: app.mostrar_frame("TestEndPoint"))
    app_menu.add_command(
        label="Comparar reportes", command=lambda: app.mostrar_frame("CompareReport"))

    # Menú de anexos

    app_menu = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Anexos", menu=app_menu)
    app_menu.add_command(
        label="Anexos en lote", command=lambda: app.mostrar_frame("BatchTest"))

    # Menú de ayuda

    ayuda_menu = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Ayuda", menu=ayuda_menu)
    ayuda_menu.add_command(label="Acerca de...", command=show_version)
    ayuda_menu.add_command(label="Salir", command=lambda: quit_app(app))


def quit_app(app):
    """Función para mostrar pedir confirmación antes de salir"""
    respuesta = messagebox.askyesno(
        "Confirmar salida", "¿Está seguro de que desea salir?")
    if respuesta:
        app.quit()


def show_version():
    """Función para mostrar la versión de la interfaz"""
    version = "GENOS 1.0.1"
    fecha = "Mayo 2024"
    descripcion = "Software diseñado para pruebas"
    messagebox.showinfo("INFO", f"{version}\n{fecha}\n{descripcion}")
