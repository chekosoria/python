"""
Aplicacion para probar el metodo GET de endpoints usando CURL
"""
import tkinter as tk
from tkinter import messagebox
import os
import csv
from datetime import datetime
import logging
import subprocess


class endpoint_tester:
    """Clase para crear la interfaz de usuario"""

    def __init__(self, master):
        self.master = master
        master.title("Endpoint Tester")
        master.geometry("600x600")
        master.resizable(0, 0)
        master.iconbitmap("code3.ico")
        master.config(cursor="hand2")

        self.setup_logging()

        self.label_alias = tk.Label(
            master, text="Asigna un Alias el Endpoint:")
        self.entry_alias = tk.Entry(master, width=70)
        self.label_url = tk.Label(
            master, text="Ingresa la URL del Endpoint:")
        self.entry_url = tk.Entry(master, width=70)
        self.button_add_endpoint = tk.Button(
            master, text="Agregar Endpoint", activeforeground="#F50743", command=self.add_endpoint)

        self.label_select_endpoint = tk.Label(
            master, text="Seleccionar Endpoint(s):")
        self.endpoint_var = tk.StringVar(master)
        # Variable para almacenar los endpoints seleccionados
        self.endpoint_var.set("")
        self.endpoint_listbox = tk.Listbox(
            master, selectmode=tk.MULTIPLE, width=70)
        self.button_test_endpoints = tk.Button(
            master, text="Probar Endpoints",
            activeforeground="#F50743", command=self.test_endpoints)

        self.label_status = tk.Label(master, text="Estado:")
        self.status_text = tk.Text(master, height=10, width=70)
        self.status_text.configure(bg="black", fg="white")

        self.label_alias.grid(row=0, column=0)
        self.entry_alias.grid(row=0, column=1)
        self.label_url.grid(row=1, column=0)
        self.entry_url.grid(row=1, column=1)
        self.button_add_endpoint.grid(row=3, columnspan=2)
        self.label_select_endpoint.grid(row=5, column=0)
        self.endpoint_listbox.grid(row=5, column=1)
        self.button_test_endpoints.grid(row=7, columnspan=2)
        self.label_status.grid(row=9, column=0)
        self.status_text.grid(row=10, columnspan=2)

        self.endpoints = {}

    def setup_logging(self):
        """Funcion para crear log"""
        log_filename = os.path.join(os.path.dirname(
            os.path.abspath(__file__)), "endpoint_tester.log")
        logging.basicConfig(filename=log_filename, level=logging.DEBUG,
                            format='%(asctime)s - %(levelname)s - %(message)s')

    def load_endpoints_from_file(self):
        """Funcion para cargar endpoints existentes"""
        current_dir = os.path.dirname(os.path.abspath(__file__))
        config_file = os.path.join(current_dir, "endpoints.csv")
        if os.path.exists(config_file):
            with open(config_file, 'r', encoding="latin-1") as csvfile:
                csv_reader = csv.reader(csvfile)
                for row in csv_reader:
                    self.endpoints[row[0]] = row[1]
        self.update_endpoint_listbox()
        logging.info("Endpoints cargados correctamente")

    def add_endpoint(self):
        """Funcion para agregar un nuevo endpoint"""
        alias = self.entry_alias.get()
        url = self.label_url.cget("text")  # Obtiene la URL del label_url
        if alias:
            # Agrega el alias y la URL al diccionario de endpoints
            self.endpoints[alias] = url
            self.update_endpoint_listbox()
            self.entry_alias.delete(0, 'end')
            self.entry_url.delete(0, 'end')
            messagebox.showinfo("exito", "Endpoint agregado correctamente.")
            logging.info("Endpoint agregado: %s", alias)
        else:
            messagebox.showerror("Error", "Alias es un campo obligatorio.")

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

    def update_endpoint_listbox(self):
        """Funcion para actualizar la lista de endpoints disponibles"""
        self.endpoint_listbox.delete(0, tk.END)
        for endpoint in self.endpoints.keys():
            self.endpoint_listbox.insert(tk.END, endpoint)

    def diferencia_horas(self, start_time, end_time):
        # Calcular la diferencia de tiempo en segundos
        diferencia_segundos = (end_time - start_time).total_seconds()

        # Calcular las horas, minutos y segundos de la diferencia
        horas = int(diferencia_segundos // 3600)
        minutos = int((diferencia_segundos % 3600) // 60)
        segundos = int(diferencia_segundos % 60)

        # Devolver la diferencia en formato hh:mm:ss
        return '{:02}:{:02}:{:02}'.format(horas, minutos, segundos)

    def test_endpoints(self):
        """Funcion para probar endpoints"""
        selected_indices = self.endpoint_listbox.curselection()
        if not selected_indices:
            messagebox.showerror(
                "Error", "Seleccione al menos un endpoint para probar.")
            return

        selected_endpoints = [self.endpoint_listbox.get(
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
                        command = ["curl", "-k", url]
                        process = subprocess.Popen(
                            command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
                        stdout, stderr = process.communicate()
                        if process.returncode == 0:
                            end_time = datetime.now()
                            # elapsed_time = (
                            #     end_time - start_time).total_seconds()
                            elapsed_time = self.diferencia_horas(
                                start_time, end_time)
                            self.status_text.insert(tk.END, f"{datetime.now(
                            )} - Se ha generado el reporte {alias} en: {elapsed_time} segundos\n")
                            self.download_file(
                                alias, start_time, end_time, elapsed_time, "Completado")
                            success = True
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

    def download_file(self, alias, start_time, end_time, elapsed_time, status):
        """Funcion para almacenar el resultado de la prueba en un CSV"""
        current_date = datetime.now().strftime("%Y-%m-%d")
        csv_filename = f"endpoint_log_{current_date}.csv"
        with open(csv_filename, 'a', newline='', encoding="latin-1") as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow([alias, start_time.strftime(
                "%H:%M:%S"), end_time.strftime("%H:%M:%S"), elapsed_time, status])
        # messagebox.showinfo("exito", f"La informacion de la prueba del reporte: \n {
        #                    alias} \n Ha sido guardada en el archivo: \n {csv_filename}.")
        logging.info("Registro de prueba guardado en %s: %s, %s, %s, %s, %s",
                     csv_filename, alias, start_time, end_time, elapsed_time, status)


def main():
    """Funcion principal
    carga interfaz y datos de endpoints existentes
    """
    root = tk.Tk()
    app = endpoint_tester(root)
    app.load_endpoints_from_file()
    root.mainloop()


if __name__ == "__main__":
    main()
