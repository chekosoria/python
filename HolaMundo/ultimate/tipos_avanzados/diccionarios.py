"""Diccionarios en Python"""

# Solo aceptan string como llaves, los valores
# pueden ser de cualquier tipo de dato
# Se definen ente {} y cada valor debe llevar
# "llave":valor

punto = {"x": 25, "y": 50}

print(punto)

# Para imprimir solo el valor se usa la llave como
# argumento variable["llave"]

print(punto["x"])
print(punto["y"])

punto["z"] = 45

print(punto)

# Otra forma de obtener solo un valor del diccionario

print(punto.get("z"))

# Si la llave no existe devuelve none

print(punto.get("j"))

# Si la llave no existe devuelve none se le puede asignar
# un valor por default

print(punto.get("j", -15))

# Para borrar un valor del diccionario se puede usar
# del diccionario["llave"] o
# del(diccionario["llave"]) este manda error con Pylance

# del punto["x"]
# del (punto["y"])

# print(punto)

# Para acceder a todos los elementos del diccionario

for llave, valor in punto.items():
    print(f"{llave} = {valor}")


usuarios = [
    {"id": 1, "nombre": "root"},
    {"id": 2, "nombre": "Homer"},
    {"id": 3, "nombre": "Peter"},
    {"id": 4, "nombre": "Rick"}
]

for usuario in usuarios:
    print(usuario["nombre"])
