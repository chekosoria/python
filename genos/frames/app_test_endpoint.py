"""Pantalla de la herramienta para probar Endpoints"""
import tkinter as tk
import logging
from tkinter import messagebox, END
import os
import csv
from datetime import datetime, timedelta
import subprocess
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


class EndPointTest(tk.Frame):
    """Pantalla para probar Endpoints"""

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        # self.logger = configurar_logger()
        # self.logger.info("Inicializando pantalla para probar Endpoints")
        self.logger = logging.getLogger(__name__)
        self.logger.info(
            "Inicializando pantalla para probar Endpoints")

        # Crear contenedor principal para centrar los elementos
        container = tk.Frame(self)
        container.pack(expand=True, fill="both")

        # Crear título
        label_titulo = tk.Label(
            container, text="Probar Endpoints", font=("Helvetica", 24, "bold"))
        label_titulo.grid(row=0, column=0, columnspan=2, pady=20)

        # Ruta del directorio actual
        current_directory = os.path.dirname(os.path.realpath(__file__))

        # Cargar y convertir el icono
        icon_path = os.path.join(current_directory, "help.png")
        help_image = Image.open(icon_path)
        help_icon = ImageTk.PhotoImage(help_image)
        icon_exe_path = os.path.join(current_directory, "play.png")
        exe_image = Image.open(icon_exe_path)
        exe_icon = ImageTk.PhotoImage(exe_image)

        # Crear botón con icono
        self.button_help = tk.Button(
            container, image=help_icon, command=self.show_help)
        self.button_exe = tk.Button(
            container, image=exe_icon, command=self.test_endpoints)
        # Referencia para evitar que se recolecte basura
        self.button_help.image = help_icon
        self.button_exe.image = exe_icon

        # Widget para mostrar y seleccionar los endpoints seleccionados
        self.label_select = tk.Label(
            container, text="Seleccionar Endpoint(s):", font=("Helvetica", 12, "bold"))
        self.listbox_endpoints = tk.Listbox(container, width=70, height=10)

        # Variable para almacenar los endpoints seleccionados
        self.endpoint_var = tk.StringVar(container)
        self.endpoint_var.set("")
        self.listbox_endpoints = tk.Listbox(
            container, selectmode=tk.MULTIPLE, width=70)

        # Widget para mostrar el estado de la prueba
        self.label_status = tk.Label(
            container, text="Estado:", font=("Helvetica", 12, "bold"))
        self.status_text = tk.Text(container, height=10, width=70)
        self.status_text.configure(bg="black", fg="white")

        # Ubicar los widgets en el contenedor
        self.button_help.grid(row=2, column=0, columnspan=2, pady=5)
        self.label_select.grid(row=3, column=0, sticky="w")
        self.listbox_endpoints.grid(
            row=4, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")
        self.button_exe.grid(row=5, column=0, columnspan=2, pady=5)
        self.label_status.grid(row=6, column=0, sticky="w")
        self.status_text.grid(row=7, column=0, columnspan=2,
                              padx=5, pady=5, sticky="nsew")

        # Centrar el contenedor en la ventana principal
        container.grid_rowconfigure(0, weight=0)
        container.grid_rowconfigure(1, weight=0)
        container.grid_rowconfigure(2, weight=0)
        container.grid_rowconfigure(3, weight=0)
        container.grid_rowconfigure(4, weight=0)
        container.grid_rowconfigure(5, weight=0)
        container.grid_rowconfigure(6, weight=0)
        container.grid_rowconfigure(7, weight=0)
        container.grid_columnconfigure(0, weight=1)
        container.grid_columnconfigure(1, weight=1)

        # Inicializar diccionario de endpoints
        self.endpoints = {}

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
                    self.endpoints[row[0]] = row[1]
        self.update_listbox_endpoints()

    def update_listbox_endpoints(self):
        """Funcion para actualizar la lista de endpoints disponibles"""
        self.listbox_endpoints.delete(0, END)
        for endpoint in self.endpoints.keys():
            self.listbox_endpoints.insert(END, endpoint)

    def get_endpoint_from_csv(self, alias):
        """Funcion para obtener la URL de los endpoints existentes a partir del alias"""
        current_dir = os.path.dirname(os.path.abspath(__file__))
        config_file = os.path.join(current_dir, "endpoints.csv")
        if os.path.exists(config_file):
            with open(config_file, 'r', encoding="latin-1") as csvfile:
                csv_reader = csv.reader(csvfile)
                for row in csv_reader:
                    if row[0] == alias:
                        return row[1]
        return None

    def test_endpoints(self):
        """Funcion para probar endpoints"""
        selected_indices = self.listbox_endpoints.curselection()
        if not selected_indices:
            messagebox.showerror(
                "Error", "Seleccione al menos un endpoint para probar.")
            return

        selected_endpoints = [self.listbox_endpoints.get(
            i) for i in selected_indices]
        for alias in selected_endpoints:
            url = self.endpoints.get(alias)
            if url:
                start_time = datetime.now()
                self.status_text.insert(
                    tk.END, f"Iniciando prueba del endpoint {alias}...\n")
                self.status_text.see(tk.END)
                self.master.update()
                retry_count = 3  # Numero maximo de reintentos
                retry = 0
                success = False
                while retry < retry_count and not success:
                    try:
                        created_file = f"{alias}.txt"
                        command = ["curl", "-o", created_file, "-k", url]
                        process = subprocess.Popen(
                            command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
                        stdout, stderr = process.communicate()
                        if process.returncode == 0:
                            end_time = datetime.now()
                            elapsed_time_seconds = (
                                end_time - start_time).total_seconds()

                            # Convertir a formato hh:mm:ss
                            elapsed_timedelta = timedelta(
                                seconds=elapsed_time_seconds)
                            elapsed_time_formatted = str(elapsed_timedelta)

                            # Leer el contenido del archivo para obtener el nombre
                            # generado por el endpoint
                            with open(created_file, "r", encoding="latin-1") as f:
                                # Leer y quitar espacios y caracteres de nueva línea
                                generated_filename = f.readline().strip()

                            self.status_text.insert(
                                tk.END, f"{datetime.now(
                                )} - Se ha generado el reporte {alias} en {
                                    elapsed_time_formatted} segundos\n"
                            )

                            # Registrar el resultado en el log y añadir el nombre del
                            # archivo generado por el endpoint
                            self.download_file(
                                alias,
                                start_time,
                                end_time,
                                elapsed_time_formatted,
                                "Completado",
                                generated_filename,
                            )
                            success = True

                            # Eliminar el archivo para evitar acumulación de archivos basura
                            if os.path.exists(created_file):
                                os.remove(created_file)
                        else:
                            self.status_text.insert(tk.END, f"Error al generar el reporte {
                                                    alias}: {stderr.decode()}\n")
                            retry += 1
                            if retry < retry_count:
                                self.status_text.insert(
                                    tk.END, f"Reintentando ({retry}/{retry_count})...\n")
                    except Exception as e:
                        self.status_text.insert(
                            tk.END, f"Error al generar el reporte {alias}: {str(e)}\n")
                        retry += 1
                        if retry < retry_count:
                            self.status_text.insert(
                                tk.END, f"Reintentando ({retry}/{retry_count})...\n")
                if not success:
                    self.status_text.insert(tk.END, f"No se pudo generar el reporte {
                                            alias} despues de {retry_count} intentos.\n")
            else:
                self.status_text.insert(
                    tk.END, f"No se encontro la URL para el alias {alias}\n")
        messagebox.showinfo("exito", "Prueba completada.")
        self.logger.info("Prueba completada.")

    def download_file(self, alias, start_time, end_time, elapsed_time_formatted,
                      status, generated_filename):
        """Función para almacenar el resultado de la prueba en un CSV"""
        current_date = datetime.now().strftime("%Y-%m-%d")
        csv_filename = f"endpoint_log_{current_date}.csv"
        with open(csv_filename, 'a', newline='', encoding="latin-1") as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow([alias, start_time.strftime("%H:%M:%S"), end_time.strftime(
                "%H:%M:%S"), elapsed_time_formatted, status, generated_filename])
        self.logger.info("Registro de prueba guardado en %s: %s, %s, %s, %s, %s",
                         csv_filename, alias, start_time, end_time, elapsed_time_formatted, status)
