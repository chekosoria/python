"""Ordenar listas en Python"""
numeros = [1, 2, 3, 4, 9, 5, 7, 6, 15, 11]

numeros.sort()

print(numeros)

numeros.sort(reverse=True)

print(numeros)

numeros2 = sorted(numeros)

print(numeros)
print(numeros2)

numeros2 = sorted(numeros, reverse=True)

print(numeros2)

usuarios = [[4, "Homero"], [1, "Bart"], [5, "Cartman"]]

usuarios.sort()

print(usuarios)


def ordena(elemento):
    """Función paa retornar el segundo elemento de una tupla"""
    return elemento[1]


usr = [["Tom", 2], ["Al", 1], ["Anne", 5]]

usr.sort(key=ordena)

print(usr)

usr.sort(key=ordena, reverse=True)

print(usr)


usr.sort(key=lambda el: el[1], reverse=True)

print(usr)
