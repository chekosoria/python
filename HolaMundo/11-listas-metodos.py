# Se agrega una lista como variable
lenguajes = ["Python", "Ruby", "PHP", "Javascript", "Java"]
"""
Para agregar un elemento a la lista se utiliza el método insert al cuál se
le deben pasar 2 parámetros separados por una "," primero se pasa el índice
y después el valor del elemento
"""
# Se inserta el valor Go en el índice 3
lenguajes.insert(3, "Go")
# Se inserta el valor C en el índice 0
lenguajes.insert(0, "C")
# Se imprime la lista completa
print(lenguajes)
"""
Para eliminar un elemento de la lista se utiliza el método remove al cuál se
le debe pasar como parámetro el valor que se quiere eliminar
"""
# Se elimina el elemento con valor Ruby
lenguajes.remove("Ruby")
# Se imprime la lista completa
print(lenguajes)
# Para verificar si un dato existe en la lista se utiliza in dentro del print
print("PHP" in lenguajes)
# Para "limpiar" los datos dentro de la lista se usa clear()
#lenguajes.clear()
# Se imprime la lista completa
print(lenguajes)
# Para saber cuantos elementos tiene una lista se utiliza len() pasando como parámetro el nombre de la lista
print(len(lenguajes))