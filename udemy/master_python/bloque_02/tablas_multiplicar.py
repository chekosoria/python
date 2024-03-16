"""
Tablas de multiplicar usando funciones
"""


def tabla(numero):
    """Función para mostrar la tabla de multiplicar
       del número ingresado por el usuario
    """
    print(f"\n*** Mostrando la tabla del {numero} ***")
    for num in range(1, 11):
        resultado = numero * num
        print(f"{numero} x {num} = {resultado}")
    print("\n******************************")


x = int(input("Ingrese un número: "))

tabla(x)
