"""App principal"""
import tkinter as tk
from menus import crear_menus
from frames.app_home import Home
from frames.app_add_endpoint import AddEndPoint
from frames.app_edit_endpoint import EditEndPoint
from frames.app_test_endpoint import TestEndPoint
from frames.app_compare_report import CompareReport
from frames.app_batch_test import BatchTest
from logging_config import configurar_logger


class Genos(tk.Tk):
    """Creación de interfaz principal"""

    def __init__(self):
        super().__init__()

        version = 1.0

        self.logger = configurar_logger()
        self.logger.info("Iniciando GENOS %s", version)
        self.title("GENOS")
        self.geometry("880x700")
        self.iconbitmap("bender.ico")
        self.frames = {}
        self.crear_frames()
        self.mostrar_frame("Home")  # Muestra la app por defecto

    def crear_frames(self):
        """Método para crear frames"""
        for F in (Home, AddEndPoint, EditEndPoint, TestEndPoint, CompareReport, BatchTest):
            page_name = F.__name__
            frame = F(parent=self, controller=self)
            self.frames[page_name] = frame
            self.logger.info("Creando frame para %s", page_name)
            frame.grid(row=0, column=0, sticky="nsew")

    def mostrar_frame(self, page_name):
        """Método para mostrar frames"""
        self.logger.info("Mostrando frame %s", page_name)
        frame = self.frames[page_name]
        frame.tkraise()
        frame.event_generate("<<ShowFrame>>")


if __name__ == "__main__":
    app = Genos()
    crear_menus(app)
    app.mainloop()
