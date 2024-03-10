"""Buscar elementos en una lista"""
mascotas = ["Camila", "Puka", "Coca", "Ninfa", "Pancho", "Darky", "Camila"]

# Regresa el índice del elemento buscado
print(mascotas.index("Puka"))

# Si se quiere asegurar de que no se obtendrá un
# error aunque no se encuentre el elemento

if "Darky" in mascotas:
    print(mascotas.index("Darky"))

# Contar cuantas veces está un elemento

print(mascotas.count("Camila"))
