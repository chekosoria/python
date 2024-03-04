"""Listas"""

# Se agrega una lista como variable

lenguajes = ["Python", "Ruby", "PHP", "Javascript", "Java"]

# Se imprimen todos los elementos de la lista

print(lenguajes)

# Se muestra el elemento índice 1 de la lista

print(lenguajes[1])

# Se actualiza el valor del índice 1 de la lista

lenguajes[1] = "Go"

# Se muestra el elemento índice 1 de la lista el cuál ha sido actualizado

print(lenguajes[1])

# Si se llama un elemento de la lista con un número negativo se comienza
# a contar los índices desde el último elemto el cuál sería -1

print(lenguajes[-1])

# Para llamar un rango de elemento de una lista se utliza : dentro de [] i.e. print(lenguajes[1:3])
# donde 1 es el primer elemento a mostrar y 3 es el elemento siguiente al último elemento que se
# quiere mostrar.

print(lenguajes[1:3])

# Si se llama un elemento por rango y no se indica el valor inicial Python resolverá
# que el primer elemento que se quiere mostrar es el primer elemento de la lista

print(lenguajes[:3])

# Si se llama un elemento por rango y no se indica el valor final Python resolverá
# que el último elemento que se quiere mostrar es el último elemento de la lista

print(lenguajes[1:])
