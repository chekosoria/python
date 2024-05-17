"""Página principal"""
import tkinter as tk
import logging
import os
from PIL import Image, ImageTk


class Home(tk.Frame):
    """Definición de página principal"""

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.logger = logging.getLogger(__name__)
        self.logger.info("Inicializando pantalla principal")

        # Crear título
        label_titulo = tk.Label(
            self, text="Bienvenido a Genos", font=("Helvetica", 24))
        label_titulo.pack(pady=20)

        # Crear un frame para contener la imagen y centrarla
        frame_imagen = tk.Frame(self)
        frame_imagen.pack(pady=20)

        # Cargar y mostrar imagen
        current_directory = os.path.dirname(os.path.realpath(__file__))
        image_path = os.path.join(current_directory, "bug.jpg")
        self.cargar_imagen(image_path, frame_imagen)

        # Centrar el contenedor en la ventana principal
        controller.grid_rowconfigure(0, weight=0)

    def cargar_imagen(self, ruta_imagen, frame):
        """Función para cargar la imagen"""
        try:
            # Cargar la imagen
            imagen = Image.open(ruta_imagen)
            imagen = imagen.resize((333, 331), Image.Resampling.LANCZOS)
            self.imagen_tk = ImageTk.PhotoImage(imagen)

            # Crear un label para mostrar la imagen
            imagen_label = tk.Label(frame, image=self.imagen_tk)
            imagen_label.pack()
            self.logger.info("Imagen cargada correctamente")
        except Exception as e:
            self.logger.error("Error al cargar la imagen: %s", e)
