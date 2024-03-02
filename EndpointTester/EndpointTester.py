"""_summary_"""
import tkinter as tk
from tkinter import messagebox
import ssl
import os
import csv
import requests
from datetime import datetime
import logging
import threading

ssl._create_default_https_context = ssl._create_unverified_context

class EndpointTesterApp:
    def __init__(self, master):
        self.master = master
        master.title("Endpoint Tester")
        master.geometry("600x600")
        master.iconbitmap("house-stark.ico")
        master.resizable(0,0)
        master.config(cursor="hand2")
        
        self.setup_logging()

        self.label_url = tk.Label(master, text="Ingresa la URL del Endpoint:")
        self.label_alias = tk.Label(master, text="Asigna un Alias el Endpoint:")
        self.entry_url = tk.Entry(master, width=70)
        self.entry_alias = tk.Entry(master, width=70)
        self.button_add_endpoint = tk.Button(master, text="Agregar Endpoint", activeforeground="#F50743",command=self.add_endpoint)

        self.label_select_endpoint = tk.Label(master, text="Seleccionar Endpoint(s):")
        self.endpoint_var = tk.StringVar(master)
        self.endpoint_var.set("")  # Variable para almacenar los endpoints seleccionados
        self.endpoint_listbox = tk.Listbox(master, selectmode=tk.MULTIPLE,width=70)
        self.button_test_endpoints = tk.Button(master, text="Probar Endpoints", activeforeground="#F50743", command=self.test_endpoints)

        self.label_status = tk.Label(master, text="Estado:")
        self.status_text = tk.Text(master, height=10, width=70)
        self.status_text.configure(bg="black", fg="white")

        self.label_url.grid(row=0, column=0)
        self.label_alias.grid(row=1, column=0)
        self.entry_url.grid(row=0, column=1)
        self.entry_alias.grid(row=1, column=1)
        self.button_add_endpoint.grid(row=3, columnspan=2)
        self.label_select_endpoint.grid(row=5, column=0)
        self.endpoint_listbox.grid(row=5, column=1)
        self.button_test_endpoints.grid(row=7, columnspan=2)
        self.label_status.grid(row=9, column=0)
        self.status_text.grid(row=10, columnspan=2)

        self.endpoints = {}

    def setup_logging(self):
        log_filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), "endpoint_tester.log")
        logging.basicConfig(filename=log_filename, level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

    def add_endpoint(self):
        url = self.entry_url.get()
        alias = self.entry_alias.get()
        if url and alias:
            self.endpoints[alias] = url
            self.save_endpoints_to_file()
            self.update_endpoint_listbox()
            self.entry_url.delete(0, 'end')
            self.entry_alias.delete(0, 'end')
            messagebox.showinfo("Éxito", "Endpoint agregado correctamente.")
            logging.info(f"Endpoint agregado: {alias} - {url}")
        else:
            messagebox.showerror("Error", "URL y Alias son campos obligatorios.")

    def save_endpoints_to_file(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        config_file = os.path.join(current_dir, "endpoints.csv")
        with open(config_file, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            for alias, url in self.endpoints.items():
                csv_writer.writerow([alias, url])
        logging.info("Endpoints guardados en el archivo endpoints.csv")

    def load_endpoints_from_file(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        config_file = os.path.join(current_dir, "endpoints.csv")
        if os.path.exists(config_file):
            with open(config_file, 'r') as csvfile:
                csv_reader = csv.reader(csvfile)
                for row in csv_reader:
                    alias, url = row
                    self.endpoints[alias] = url
        self.update_endpoint_listbox()
        logging.info("Endpoints cargados correctamente")

    def update_endpoint_listbox(self):
        self.endpoint_listbox.delete(0, tk.END)
        for endpoint in self.endpoints.keys():
            self.endpoint_listbox.insert(tk.END, endpoint)

    def test_endpoints(self):
        selected_indices = self.endpoint_listbox.curselection()
        if not selected_indices:
            messagebox.showerror("Error", "Seleccione al menos un endpoint para probar.")
            return

        selected_endpoints = [self.endpoint_listbox.get(i) for i in selected_indices]
        for alias in selected_endpoints:
            url = self.endpoints.get(alias)
            if url:
                self.status_text.insert(tk.END, f"Iniciando prueba del endpoint {alias}...\n")
                self.status_text.see(tk.END)
                self.master.update()
                threading.Thread(target=self.send_request, args=(url, alias)).start()
            else:
                self.status_text.insert(tk.END, f"No se encontró la URL para el alias {alias}\n")
        messagebox.showinfo("Éxito", "Prueba iniciada.")

    def send_request(self, url, alias):
        try:
            response = requests.get(url, timeout=1800, verify=False)  # Timeout de 30 minutos y no verifica el certificado
            self.handle_response(response, alias)
        except requests.RequestException as e:
            self.handle_error(e, alias)
        messagebox.showinfo("Éxito", "Prueba completada.")

    def send_request(self, url, alias):
        start_time = datetime.now()
        try:
            response = requests.get(url, timeout=1800, verify=False)  # Timeout de 30 minutos y no verifica el certificado
            self.handle_response(response, alias, start_time)
        except requests.RequestException as e:
            self.handle_error(e, alias, start_time)

    def handle_response(self, response, alias, start_time):
        end_time = datetime.now()
        elapsed_time = (end_time - start_time).total_seconds()
        self.status_text.insert(tk.END, f"{datetime.now()} - Se ha generado el reporte {alias} en: {elapsed_time} segundos\n")
        # Verifica si la solicitud fue exitosa (código de estado 200)
        if response.status_code == 200:
            self.download_file(response, alias, start_time, end_time, elapsed_time, "Completado")
        else:
            self.status_text.insert(tk.END, f"La solicitud al endpoint {alias} no fue exitosa (código de estado: {response.status_code})\n")

    def handle_error(self, error, alias, start_time):
        end_time = datetime.now()
        elapsed_time = (end_time - start_time).total_seconds()
        if isinstance(error, requests.Timeout):
            self.status_text.insert(tk.END, f"Tiempo de espera agotado al generar el reporte {alias}\n")
        else:
            self.status_text.insert(tk.END, f"Error al generar el reporte {alias}: {str(error)}\n")
        self.download_file(None, alias, start_time, end_time, elapsed_time, "Error")


    def download_file(self, response, alias, start_time, end_time, elapsed_time, status):
        current_date = datetime.now().strftime("%Y-%m-%d")
        csv_filename = f"endpoint_log_{current_date}.csv"
        with open(csv_filename, 'a', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow([alias, start_time.strftime("%H:%M:%S"), end_time.strftime("%H:%M:%S"), elapsed_time, status])
        messagebox.showinfo("Éxito", f"La información de la prueba del reporte: \n {alias} \n Ha sido guardada en el archivo: \n {csv_filename}.")
        logging.info(f"Registro de prueba guardado en {csv_filename}: {alias}, {start_time}, {end_time}, {elapsed_time}, {status}")

def main():
    root = tk.Tk()
    app = EndpointTesterApp(root)
    app.load_endpoints_from_file()
    root.mainloop()

if __name__ == "__main__":
    main()
