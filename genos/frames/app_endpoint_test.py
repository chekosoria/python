"""Pantalla de la herramienta para probar Endpoints"""
import tkinter as tk
import logging
from tkinter import messagebox, END
import os
import csv
from PIL import Image, ImageTk


class EndPointTest(tk.Frame):
    """Pantalla para probar Endpoints"""

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.logger = logging.getLogger(__name__)
        self.logger.info("Inicializando pantalla para probar Endpoints")

        # Crear contenedor principal para centrar los elementos
        container = tk.Frame(self)
        container.pack(expand=True, fill="both")

        # Crear título
        label_titulo = tk.Label(
            container, text="Probar Endpoints", font=("Helvetica", 24))
        label_titulo.grid(row=0, column=0, columnspan=2, pady=20)

        # Ruta del directorio actual
        current_directory = os.path.dirname(os.path.realpath(__file__))

        # Cargar y convertir el icono
        icon_path = os.path.join(current_directory, "help.png")
        help_image = Image.open(icon_path)
        help_icon = ImageTk.PhotoImage(help_image)

        # Crear botón con icono
        self.button_help = tk.Button(
            container, image=help_icon, command=self.show_help)
        # Referencia para evitar que se recolecte basura
        self.button_help.image = help_icon

        # Widget para mostrar y seleccionar los endpoints agregados
        self.listbox_endpoints = tk.Listbox(container, width=70, height=10)

        # Ubicar los widgets en el contenedor
        self.button_help.grid(row=2, column=0, columnspan=2, pady=5)
        self.listbox_endpoints.grid(
            row=3, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

        # Centrar el contenedor en la ventana principal
        container.grid_rowconfigure(0, weight=0)
        container.grid_rowconfigure(1, weight=0)
        container.grid_rowconfigure(2, weight=0)
        container.grid_columnconfigure(0, weight=1)
        container.grid_columnconfigure(1, weight=1)

        # Cargar los endpoints existentes
        self.cargar_endpoints()

    def show_help(self):
        """Método para mostrar opciones de pruebas"""
        individual = """
        ********************************
        Probar 1 Endpoint
        ********************************
        - Dar clic en el Endpoint
        - Dar clic en el botón Comenzar
                        """
        lote = """
        ********************************
        Probar 2 o más Endpoints
        ********************************
        - Dar clic en cada Endpoint
        - Dar clic en el botón Comenzar
                        """
        messagebox.showinfo("Ayuda", f"{individual}\n{lote}")

    def cargar_endpoints(self):
        """Cargar los endpoints existentes desde el archivo de configuración"""
        current_dir = os.path.dirname(os.path.abspath(__file__))
        config_file = os.path.join(current_dir, "endpoints.csv")
        if os.path.exists(config_file):
            with open(config_file, 'r', encoding="latin-1") as csvfile:
                csv_reader = csv.reader(csvfile)
                for row in csv_reader:
                    self.listbox_endpoints.insert(END, row[0])
