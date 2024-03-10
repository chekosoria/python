"""Agregar y eliminar elementos de una lista en Python"""
mascotas = ["Camila", "Puka", "Coca", "Camila", "Ninfa", "Pancho", "Darky"]

# Para insertar valores en una lista lista.insert(índice, valor)

mascotas.insert(1, "Daly")

print(mascotas)

# Para insertar valores al final de una lista lista.append(valor)

mascotas.append("Lola")

print(mascotas)


# Para eliminar elementos de una lista lista.remove(valor)
# solo elimina la primera coincidencia

mascotas.remove("Camila")

print(mascotas)


# Para eliminar el último elemento de una lista
# lista.pop()

mascotas.pop()

print(mascotas)

#  Para eliminar elemento con pop en () se pasa el índice

mascotas.pop(3)

print(mascotas)

# Para eliminar elemento de una lista del lista[indice]

del mascotas[0]

print(mascotas)

# Para limpiar por completo la lista lista.clear()

mascotas.clear()

print(mascotas)
