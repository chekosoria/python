"""App principal"""
import tkinter as tk
from menus import crear_menus
from frames.app_home import Home
from frames.anexos_lote.al_add_endpoint import AddEndPointAl
from frames.anexos_lote.al_edit_endpoint import EditEndPointAl
from frames.anexos_lote.al_test_endpoint import TestEndPointAl
from frames.anexos_lote.al_batch_test import BatchTestAl
from frames.anexos.ai_add_endpoint import AddEndPointAi
from frames.anexos.ai_edit_endpoint import EditEndPointAi
from frames.anexos.ai_test_endpoint import TestEndPointAi
from frames.anexos.ai_batch_test import BatchTestAi
from frames.varios.app_compare_report import CompareReport
from logging_config import configurar_logger


class Genos(tk.Tk):
    """Creación de interfaz principal"""

    def __init__(self):
        super().__init__()

        version = 1.0

        self.logger = configurar_logger()
        self.logger.info("Iniciando GENOS %s", version)
        self.title("GENOS")
        self.geometry("1100x800")
        self.iconbitmap("bender.ico")
        self.frames = {}
        self.crear_frames()
        self.mostrar_frame("Home")  # Muestra la app por defecto

    def crear_frames(self):
        """Método para crear frames"""
        for F in (Home,
                  AddEndPointAl,
                  EditEndPointAl,
                  TestEndPointAl,
                  BatchTestAl,
                  AddEndPointAi,
                  EditEndPointAi,
                  TestEndPointAi,
                  BatchTestAi,
                  CompareReport):
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
