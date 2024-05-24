"""Herramienta para editar Enpoints"""
import tkinter as tk
from tkinter import ttk, messagebox
import logging
import os
import sqlite3
from PIL import Image, ImageTk
from utils.db_utils import inicializar_base_de_datos, obtener_conexion


def configurar_logger():
    """Función para configurar log"""
    sistema = "Genos"

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    # Formato del log
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Manejador para el archivo principal
    file_handler = logging.FileHandler(f"{sistema.lower()}.log")
    file_handler.setFormatter(formatter)

    # Manejador para la consola
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)

    # Añadir los manejadores al logger
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    return logger


class EditEndPoint(tk.Frame):
    """Pantalla editar Endpoints"""

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.logger = logging.getLogger(__name__)
        self.logger.info(
            "Inicializando pantalla para editar Endpoints")

        # Crear contenedor principal para centrar los elementos
        container = tk.Frame(self)
        container.pack(expand=True, fill="both")

        # Crear título
        label_titulo = tk.Label(
            container, text="Editar Endpoints", font=("Helvetica", 24, "bold"))
        label_titulo.grid(row=0, columnspan=3, pady=5, sticky="n")

        # Widgets para ingresar alias, URL y parámetros del endpoint
        self.label_id = tk.Label(
            container, text="ID del Endpoint:", font=("Helvetica", 12, "bold"))
        self.label_id_value = tk.Label(
            container, font=("Helvetica", 12, "bold"))
        self.label_alias = tk.Label(
            container, text="Alias del Endpoint:", font=("Helvetica", 12, "bold"))
        self.entry_alias = tk.Entry(container, width=30)
        self.label_url = tk.Label(
            container, text="URL del Endpoint:", font=("Helvetica", 12, "bold"))
        self.entry_url = tk.Entry(container, width=30)
        self.label_params = tk.Label(
            container, text="Parámetros del Endpoint:", font=("Helvetica", 12, "bold"))
        self.entry_params = tk.Entry(container, width=30)
        self.label_download_url = tk.Label(
            container, text="URL de descarga:", font=("Helvetica", 12, "bold"))
        self.entry_download_url = tk.Entry(container, width=30)

        # Ruta del directorio actual
        current_directory = os.path.dirname(os.path.realpath(__file__))

        # Cargar y convertir los iconos
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
            container, image=save_icon, command=self.guardar_cambios)
        self.button_cancel = tk.Button(
            container, image=cancel_icon, command=self.cancelar_edicion)
        self.button_clean = tk.Button(
            container, image=clean_icon, command=self.limpiar_formulario)
        # Referencia para evitar que se recolecte basura
        self.button_add_endpoint.image = save_icon
        self.button_cancel.image = cancel_icon
        self.button_clean.image = clean_icon

        # Widget para mostrar y seleccionar los endpoints agregados
        self.tree = ttk.Treeview(container, columns=(
            "ID", "Alias", "URL", "Parametros", "URL descarga"), show='headings')
        self.tree.heading("ID", text="ID")
        self.tree.heading("Alias", text="Alias")
        self.tree.heading("URL", text="URL")
        self.tree.heading("Parametros", text="Parámetros")
        self.tree.heading("URL descarga", text="URL descarga")
        self.tree.column("ID", width=50)
        self.tree.column("Alias", width=150)
        self.tree.column("URL", width=250)
        self.tree.column("Parametros", width=200)
        self.tree.column("URL descarga", width=200)
        self.tree.bind("<Double-1>", self.on_double_click)

        # Ubicar los widgets en el contenedor
        self.label_id.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.label_id_value.grid(row=1, column=1, padx=5, pady=5, sticky="w")
        self.label_alias.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.entry_alias.grid(row=3, columnspan=3,
                              padx=5, pady=5, sticky="nsew")
        self.label_url.grid(row=4, column=0, padx=5, pady=5, sticky="w")
        self.entry_url.grid(row=5, columnspan=3,
                            padx=5, pady=5, sticky="nsew")
        self.label_params.grid(row=6, column=0, padx=5, pady=5, sticky="w")
        self.entry_params.grid(row=7, columnspan=3,
                               padx=5, pady=5, sticky="nsew")
        self.label_download_url.grid(
            row=8, column=0, padx=5, pady=5, sticky="w")
        self.entry_download_url.grid(row=9, columnspan=3,
                                     padx=5, pady=5, sticky="nsew")
        self.button_add_endpoint.grid(row=10, column=0, pady=5, sticky="e")
        self.button_cancel.grid(row=10, column=1, pady=5, sticky="w")
        self.button_clean.grid(row=10, column=2, pady=5, sticky="e")
        self.tree.grid(row=11, columnspan=3, padx=5, pady=5, sticky="nsew")

        # Inicializar base de datos
        inicializar_base_de_datos()

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
        container.grid_rowconfigure(8, weight=1)
        container.grid_rowconfigure(9, weight=1)
        container.grid_rowconfigure(10, weight=1)
        container.grid_rowconfigure(11, weight=1)
        container.grid_columnconfigure(0, weight=1)
        container.grid_columnconfigure(1, weight=1)
        container.grid_columnconfigure(2, weight=1)

        # Variable para almacenar el alias seleccionado y su ID
        self.selected_alias = None
        self.selected_id = None

        # Vincular el método cargar_endpoints al evento de mostrar la pantalla
        self.bind("<<ShowFrame>>", self.on_show_frame)

    def on_show_frame(self, event):
        """Cargar los endpoints existentes desde la base de datos al mostrar la pantalla"""
        self.cargar_endpoints()

    def cargar_endpoints(self):
        """Cargar los endpoints existentes desde la base de datos"""
        self.tree.delete(*self.tree.get_children())  # Limpiar Treeview
        with obtener_conexion() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT id, alias, url, parametros, download_url FROM endpoints")
            rows = cursor.fetchall()
            for row in rows:
                self.tree.insert("", tk.END, values=row)

    def on_double_click(self, event):
        """Función para manejar el doble clic en el Treeview"""
        item = self.tree.selection()[0]
        values = self.tree.item(item, "values")

        # Cargar los datos del registro seleccionado en el formulario
        self.selected_id = values[0]  # Almacenar el ID seleccionado
        self.selected_alias = values[1]  # Almacenar el alias seleccionado

        # Mostrar el ID seleccionado
        self.label_id_value.config(text=values[0])
        self.entry_alias.delete(0, tk.END)
        self.entry_alias.insert(0, values[1])
        self.entry_url.delete(0, tk.END)
        self.entry_url.insert(0, values[2])
        self.entry_params.delete(0, tk.END)
        self.entry_params.insert(0, values[3])
        self.entry_download_url.delete(0, tk.END)
        self.entry_download_url.insert(0, values[4])

    def guardar_cambios(self):
        """Guardar los cambios realizados en el registro"""
        alias = self.entry_alias.get()
        url = self.entry_url.get()
        params = self.entry_params.get()
        download_url = self.entry_download_url.get()

        if alias and url:
            try:
                with obtener_conexion() as conn:
                    cursor = conn.cursor()
                    cursor.execute(
                        """UPDATE endpoints 
                           SET alias = ?, url = ?, parametros = ?, download_url = ? 
                           WHERE id = ?""",
                        (alias, url, params, download_url, self.selected_id))
                    conn.commit()
                messagebox.showinfo(
                    "Éxito", "Endpoint actualizado correctamente.")
                self.logger.info("Endpoint actualizado: %s", alias)
                self.limpiar_formulario()
                self.cargar_endpoints()
            except sqlite3.Error as e:
                messagebox.showerror(
                    "Error", f"No se pudo actualizar el endpoint: {e}")
        else:
            messagebox.showerror("Error", "Todos los campos son obligatorios.")

    def cancelar_edicion(self):
        """Cancelar la edición y limpiar los campos del formulario"""
        self.limpiar_formulario()

    def limpiar_formulario(self):
        """Limpiar los campos del formulario"""
        self.label_id_value.config(text="")
        self.entry_alias.delete(0, tk.END)
        self.entry_url.delete(0, tk.END)
        self.entry_params.delete(0, tk.END)
        self.entry_download_url.delete(0, tk.END)
        self.selected_alias = None
        self.selected_id = None
