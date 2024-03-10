"""Comprensión de listas en Python"""

usuario = [["Tom", 2], ["Al", 1], ["Anne", 5]]

for usr in usuario:
    print(usr[0])


# nombres = []

# for usr in usuario:
#     nombres.append(usr[0])
# print(nombres)

# Transformar o map
# nombres = [expresion for item in items]

nombres = [usr[0] for usr in usuario]

print(nombres)

# Filtrar o filter

nombres = [usr for usr in usuario if usr[1] >= 2]

print(nombres)

# Filtrar y transformar

nombres = [usr[0] for usr in usuario if usr[1] >= 2]

print(nombres)

# map

names = list(map(lambda usr: usr[0], usuario))

print(names)

# filter

menos_usr = list(filter(lambda usr: usr[1] >= 2, usuario))

print(menos_usr)
