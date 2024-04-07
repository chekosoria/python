"""Muestra de elementos básicos de una interfaz gráfica"""
# Para importa módulos se usa la palabra reservada import
# import tkinter
import tkinter as tk

# Para crear una pantalla primero se debe crear una instancia con tkinter.Tk()
# El nombre puede ser cualquiera que se quiera, un estándar es root = tkinter.Tk()
root = tk.Tk()

# Para definir un título a la ventana usar el método title("texto")

root.title("Mi primera GUI")

# Para cambiar las dimensiones de la ventana usar el método geometry("123x123")
# donde se pasa como argumento las medidas en pixeles que se quieren para la ventana
# si se quiere cambiar la pocisión inicial de la venta se deben agregar los argumentos
# +123+123 donde el primer valor es X y el segundo Y

root.geometry("800x600+560+240")

# Para crear una etiqueta que pueda ser vista en la pantalla se debe crear
# una mariable con el método Label(root,text="Hola mundo")
saludo = tk.Label(root, text="Hola mundo!")
nombre = tk.Label(root, text="Soy Sergio")
mensaje = tk.Label(root, text="Estoy aprendiendo Tkinter")


# Para mostrar la etiqueta en la pantalla se debe usar el método pack() con la sintaxis
# variable.pack()
# saludo.pack()

# También se pueden ubicar los elementos de la pantalla basandose en un estilo de filas y columnas
# usando el método grid(row, column) en lugar de pack()
saludo.grid(row=0, column=0)
nombre.grid(row=1, column=0)
mensaje.grid(row=1, column=1)

# Siempre que se cree una pantalla se debe usar el método mainloop() para que la pantalla
# no se cierre en automático
root.mainloop()
