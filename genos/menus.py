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

    # Menú de Anexos
    anexos_menu = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Anexos", menu=anexos_menu)

    # Crear el submenú "Anexos por lote" dentro del menú "Anexos"
    anexos_submenu_lote = tk.Menu(anexos_menu, tearoff=0)
    anexos_menu.add_cascade(label="Anexos por lote", menu=anexos_submenu_lote)

    # Añadir comandos al submenú "Anexos por lote"
    anexos_submenu_lote.add_command(
        label="Agregar Endpoint", command=lambda: app.mostrar_frame("AddEndPointAl"))
    anexos_submenu_lote.add_command(
        label="Editar Endpoint", command=lambda: app.mostrar_frame("EditEndPointAl"))
    anexos_submenu_lote.add_command(
        label="Probar Endpoint", command=lambda: app.mostrar_frame("TestEndPointAl"))
    anexos_submenu_lote.add_command(
        label="PROD vs QA", command=lambda: app.mostrar_frame("BatchTestAl"))

    # Crear el submenú "Anexos individuales" dentro del menú "Anexos"
    anexos_submenu = tk.Menu(anexos_menu, tearoff=0)
    anexos_menu.add_cascade(label="Anexos individuales", menu=anexos_submenu)

    # Añadir comandos al submenú "Anexos individuales"
    anexos_submenu.add_command(
        label="Agregar Endpoint", command=lambda: app.mostrar_frame("AddEndPointAi"))
    anexos_submenu.add_command(
        label="Editar Endpoint", command=lambda: app.mostrar_frame("EditEndPointAi"))
    anexos_submenu.add_command(
        label="Probar Endpoint", command=lambda: app.mostrar_frame("TestEndPointAi"))
    anexos_submenu.add_command(
        label="PROD vs QA", command=lambda: app.mostrar_frame("BatchTestAi"))

    # Menú de herramientas

    app_menu = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Herramientas", menu=app_menu)
    app_menu.add_command(
        label="Comparar reportes", command=lambda: app.mostrar_frame("CompareReport"))

    # Menú de ayuda

    ayuda_menu = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Ayuda", menu=ayuda_menu)
    ayuda_menu.add_command(label="Acerca de...", command=show_version)
    ayuda_menu.add_command(label="Salir", command=lambda: quit_app(app))

    # Menú de ayuda


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
