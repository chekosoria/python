"""Pantalla de la herramienta para probar Endpoints"""
import tkinter as tk
import logging
from tkinter import ttk, messagebox, END
import os
import subprocess
import csv
from datetime import datetime, timedelta
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


class TestEndPoint(tk.Frame):
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
            container, text="Probar Endpoints", font=("Helvetica", 24, "bold"))
        label_titulo.grid(row=0, column=0, columnspan=2, pady=20)

        # Ruta del directorio actual
        current_directory = os.path.dirname(os.path.realpath(__file__))

        # Ruta del directorio principal
        pack_directory = os.path.abspath(os.path.join(current_directory, '..'))

        # Ruta del directorio media
        media_directory = os.path.join(pack_directory, 'media')

        # Cargar y convertir el icono
        icon_path = os.path.join(media_directory, "help.png")
        help_image = Image.open(icon_path)
        help_icon = ImageTk.PhotoImage(help_image)
        icon_exe_path = os.path.join(media_directory, "play.png")
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

        # Widget para mostrar y seleccionar los endpoints agregados
        self.label_select = tk.Label(
            container, text="Seleccionar Endpoint(s):", font=("Helvetica", 12, "bold"))
        self.tree_endpoints = ttk.Treeview(container, columns=(
            "ID", "Alias", "URL", "Parametros", "URL descarga", "Ambiente"),
            show='headings', selectmode="extended")
        self.tree_endpoints.heading("ID", text="ID")
        self.tree_endpoints.heading("Alias", text="Alias")
        self.tree_endpoints.heading("URL", text="URL")
        self.tree_endpoints.heading("Parametros", text="Parámetros")
        self.tree_endpoints.heading("URL descarga", text="URL descarga")
        self.tree_endpoints.heading("Ambiente", text="Ambiente")
        self.tree_endpoints.column("ID", width=50)
        self.tree_endpoints.column("Alias", width=150)
        self.tree_endpoints.column("URL", width=250)
        self.tree_endpoints.column("Parametros", width=200)
        self.tree_endpoints.column("URL descarga", width=200)
        self.tree_endpoints.column("Ambiente", width=200)

        # Widget para mostrar el estado de la prueba
        self.label_status = tk.Label(
            container, text="Estado:", font=("Helvetica", 12, "bold"))
        self.status_text = tk.Text(container, height=10, width=70)
        self.status_text.configure(bg="black", fg="white")

        # Ubicar los widgets en el contenedor
        self.button_help.grid(row=2, column=0, columnspan=2, pady=5)
        self.label_select.grid(row=3, column=0, sticky="w")
        self.tree_endpoints.grid(
            row=4, columnspan=3, padx=5, pady=5, sticky="nsew")
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

        # Inicializar base de datos
        inicializar_base_de_datos()

        # Cargar los endpoints existentes
        self.cargar_endpoints()

        # Vincular el método cargar_endpoints al evento de mostrar la pantalla
        self.bind("<<ShowFrame>>", self.on_show_frame)

    def on_show_frame(self, event):
        """Cargar los endpoints existentes desde la base de datos al mostrar la pantalla"""
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
        """Cargar los endpoints existentes desde la base de datos"""
        self.tree_endpoints.delete(
            *self.tree_endpoints.get_children())  # Limpiar Treeview
        with obtener_conexion() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT id, alias, url, parametros, download_url, ambiente FROM endpoints")
            rows = cursor.fetchall()
            for row in rows:
                self.tree_endpoints.insert("", END, values=row)

    def test_endpoints(self):
        """Función para probar endpoints"""
        selected_items = self.tree_endpoints.selection()
        if not selected_items:
            messagebox.showerror(
                "Error", "Seleccione al menos un endpoint para probar.")
            return

        for item in selected_items:
            endpoint_values = self.tree_endpoints.item(item, "values")
            alias = endpoint_values[1]
            url = endpoint_values[2]
            params = endpoint_values[3]
            download = endpoint_values[4]
            env = endpoint_values[5]
            start_time = datetime.now()
            self.status_text.insert(
                tk.END, f"Iniciando prueba del endpoint {alias}...\n")
            self.status_text.see(tk.END)
            self.master.update()
            retry_count = 3  # Número máximo de reintentos
            retry = 0
            success = False
            while retry < retry_count and not success:
                try:
                    created_file = f"{alias}.txt"
                    command = ["curl", "-o", created_file, "-k", url + params]
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

                        # Registrar el resultado en el log y añadir el nombre
                        # del archivo generado por el endpoint
                        self.save_result_to_csv(
                            alias,
                            start_time,
                            end_time,
                            elapsed_time_formatted,
                            "Completado",
                            generated_filename)
                        success = True

                        if success:
                            try:
                                download_command = [
                                    "curl", "-O", "-k", download + generated_filename]
                                process = subprocess.Popen(
                                    download_command, stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE, shell=True)
                                stdout, stderr = process.communicate()
                                if process.returncode == 0:
                                    end_time = datetime.now()
                                    elapsed_time_seconds = (
                                        end_time - start_time).total_seconds()

                                    # Convertir a formato hh:mm:ss
                                    elapsed_timedelta = timedelta(
                                        seconds=elapsed_time_seconds)
                                    elapsed_time_formatted = str(
                                        elapsed_timedelta)

                                    self.status_text.insert(
                                        tk.END, f"{datetime.now()} - Se ha descargado el reporte {
                                            generated_filename} en {
                                                elapsed_time_formatted} segundos\n"
                                    )

                                    # Registrar el resultado en el log y añadir el nombre
                                    # del archivo generado por el endpoint
                                    self.save_result_to_csv(
                                        alias,
                                        start_time,
                                        end_time,
                                        elapsed_time_formatted,
                                        "Descargado",
                                        generated_filename)
                                else:
                                    self.status_text.insert(tk.END,
                                                            f"Error al descargar el reporte {
                                                                generated_filename}: {
                                                                    stderr.decode()}\n")
                            except Exception as e:
                                self.status_text.insert(tk.END, f"Error al descargar el reporte {
                                                        generated_filename}: {str(e)}\n")
                                self.logger.info("Error al descargar reporte.")
                            self.logger.info(
                                "Reporte %s descargado.", generated_filename)

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
                                        alias} después de {retry_count} intentos.\n")
        messagebox.showinfo("Éxito", "Prueba completada.")
        self.logger.info("Prueba completada.")

    def save_result_to_csv(self, alias, start_time, end_time, elapsed_time_formatted,
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
