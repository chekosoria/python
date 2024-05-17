import tkinter as tk
import logging


class App5Frame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.logger = logging.getLogger(__name__)
        self.logger.info("Inicializando App5Frame")
        label = tk.Label(self, text="App5")
        label.pack(pady=10, padx=10)
