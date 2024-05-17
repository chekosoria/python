"""Pantalla de la herramienta para agregar Endpoints"""
import tkinter as tk
import logging
from tkinter import messagebox, END
import os
import csv
from PIL import Image, ImageTk


def configurar_logger():
    """Función para configurar log"""
    SISTEMA = "Genos"

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    # Formato del log
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Manejador para el archivo principal
    file_handler = logging.FileHandler(f"{SISTEMA.lower()}.log")
    file_handler.setFormatter(formatter)

    # Manejador para la consola
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)

    # Añadir los manejadores al logger
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    return logger


class EndPointTool(tk.Frame):
    """Pantalla para agregar y editar Endpoints"""

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.logger = logging.getLogger(__name__)
        self.logger.info(
            "Inicializando pantalla para agregar y editar Endpoints")

        # Crear contenedor principal para centrar los elementos
        container = tk.Frame(self)
        container.pack(expand=True, fill="both")

        # Crear título
        label_titulo = tk.Label(
            container, text="Agregar y Editar Endpoints", font=("Helvetica", 24, "bold"))
        label_titulo.grid(row=0, columnspan=2, pady=5, sticky="n")

        # Widgets para ingresar alias y URL del endpoint
        self.label_alias = tk.Label(
            container, text="Alias del Endpoint:", font=("Helvetica", 12, "bold"))
        self.entry_alias = tk.Entry(container, width=30)
        self.label_url = tk.Label(
            container, text="URL del Endpoint:", font=("Helvetica", 12, "bold"))
        self.entry_url = tk.Entry(container, width=30)

        # Ruta del directorio actual
        current_directory = os.path.dirname(os.path.realpath(__file__))

        # Cargar y convertir el iconos
        save_icon_path = os.path.join(current_directory, "save.png")
        save_image = Image.open(save_icon_path)
        save_icon = ImageTk.PhotoImage(save_image)
        cancel_icon_path = os.path.join(current_directory, "cancel.png")
        cancel_image = Image.open(cancel_icon_path)
        cancel_icon = ImageTk.PhotoImage(cancel_image)
        icon_clean_path = os.path.join(current_directory, "clean.png")
        clean_image = Image.open(icon_clean_path)
        clean_icon = ImageTk.PhotoImage(clean_image)

        # Crear botones con icono
        self.button_add_endpoint = tk.Button(
            container, image=save_icon, command=self.agregar_endpoint)
        self.button_cancel = tk.Button(
            container, image=cancel_icon, command=self.cancelar_operacion)
        self.button_clean = tk.Button(
            container, image=clean_icon, command=self.limpiar_campos)
        # Referencia para evitar que se recolecte basura
        self.button_add_endpoint.image = save_icon
        self.button_cancel.image = cancel_icon
        self.button_clean.image = clean_icon

        # Widget para mostrar y seleccionar los endpoints agregados
        self.listbox_endpoints = tk.Listbox(container, width=50, height=10)
        self.listbox_endpoints.bind(
            "<Double-Button-1>", lambda event: self.editar_endpoint())

        # Ubicar los widgets en el contenedor
        self.label_alias.grid(row=1, column=0, padx=5, pady=5, sticky="nw")
        self.entry_alias.grid(row=2, columnspan=2,
                              padx=5, pady=5, sticky="nsew")
        self.label_url.grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.entry_url.grid(row=4, columnspan=2, padx=5,
                            pady=5, sticky="nsew")
        self.button_add_endpoint.grid(
            row=5, column=0, pady=5, sticky="e")
        self.button_cancel.grid(
            row=5, column=1, pady=5, sticky="w")
        self.listbox_endpoints.grid(
            row=7, columnspan=2, padx=5, pady=5, sticky="nsew")
        self.button_clean.grid(
            row=8, column=0, pady=5, sticky="e")

        # Cargar los endpoints existentes
        self.cargar_endpoints()

        # Centrar el contenedor en la ventana principal
        container.grid_rowconfigure(0, weight=0)
        container.grid_rowconfigure(1, weight=0)
        container.grid_rowconfigure(2, weight=0)
        container.grid_rowconfigure(3, weight=0)
        container.grid_rowconfigure(4, weight=0)
        container.grid_rowconfigure(5, weight=0)
        container.grid_rowconfigure(6, weight=0)
        container.grid_rowconfigure(7, weight=0)
        container.grid_rowconfigure(8, weight=0)
        container.grid_columnconfigure(0, weight=1)
        container.grid_columnconfigure(1, weight=1)

    def cargar_endpoints(self):
        """Cargar los endpoints existentes desde el archivo de configuración"""
        current_dir = os.path.dirname(os.path.abspath(__file__))
        config_file = os.path.join(current_dir, "endpoints.csv")
        if os.path.exists(config_file):
            with open(config_file, 'r', encoding="latin-1") as csvfile:
                csv_reader = csv.reader(csvfile)
                for row in csv_reader:
                    self.listbox_endpoints.insert(tk.END, row[0])

    def agregar_endpoint(self):
        """Función para agregar un nuevo endpoint"""
        alias = self.entry_alias.get()
        url = self.entry_url.get()

        if alias and url:
            # Agregar el endpoint al archivo de configuración
            self.guardar_endpoint(alias, url)
            # Actualizar la lista de endpoints
            self.listbox_endpoints.insert(tk.END, alias)
            messagebox.showinfo(
                "Éxito", "Endpoint agregado correctamente.")
            self.entry_alias.delete(0, 'end')
            self.entry_url.delete(0, 'end')
            self.limpiar_campos()
            self.logger.info("Endpoint agregado: %s", alias)
        else:
            messagebox.showerror(
                "Error", "Alias y URL son campos obligatorios.")

    def guardar_endpoint(self, alias, url):
        """Función para guardar el endpoint en el archivo de configuración"""
        current_dir = os.path.dirname(os.path.abspath(__file__))
        config_file = os.path.join(current_dir, "endpoints.csv")
        with open(config_file, 'a', newline='', encoding="latin-1") as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow([alias, url])

    def editar_endpoint(self):
        """Función para editar un endpoint seleccionado"""
        index = self.listbox_endpoints.curselection()
        if index:
            selected_alias = self.listbox_endpoints.get(index)
            current_dir = os.path.dirname(os.path.abspath(__file__))
            config_file = os.path.join(current_dir, "endpoints.csv")
            with open(config_file, 'r', encoding="latin-1") as csvfile:
                csv_reader = csv.reader(csvfile)
                endpoints = list(csv_reader)
            for i, (alias, url) in enumerate(endpoints):
                if alias == selected_alias:
                    self.entry_alias.delete(0, END)
                    self.entry_alias.insert(0, alias)
                    self.entry_url.delete(0, END)
                    self.entry_url.insert(0, url)
                    del endpoints[i]
                    break
            with open(config_file, 'w', newline='', encoding="latin-1") as csvfile:
                csv_writer = csv.writer(csvfile)
                csv_writer.writerows(endpoints)
            self.listbox_endpoints.delete(index)
            self.logger.info("Endpoint editado: %s", selected_alias)

    def cancelar_operacion(self):
        """Función para cancelar la operación y limpiar los campos de entrada"""
        if self.entry_alias.get() or self.entry_url.get():
            respuesta = messagebox.askyesno(
                "Confirmar", "¿Desea cancelar la operación actual?")
            if respuesta:
                self.limpiar_campos()

    def limpiar_campos(self):
        """Función para limpiar los campos de entrada"""
        self.entry_alias.delete(0, END)
        self.entry_url.delete(0, END)
