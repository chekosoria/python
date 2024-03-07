"""Key worda arguments en Python"""

# Para usar kwargs se usa doble ** antes del nombre
# del parámetro
# también se pueden mostrar solo algunos de los argumentos
# que se pasen en la llamada, para esto definir el nombre
# dentro de la función


def get_product(**datos):
    """Función para imprimir datos"""
    print(f"El producto {datos["name"]} tiene el ID {datos["id"]}")


# Al llamar la función siempre hay que darle nombre
# y valor al argumento

get_product(id="001",
            name="Iphone",
            marca="Apple")
