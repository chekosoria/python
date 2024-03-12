"""
Ejercicio 03.
     - Escribir un programa que muestre los cuadrados de los 60
       primeros números naturales. Resolverlo con for y con while
"""
print("----- Cuadrados usando FOR -----")
for n1 in range(1, 61):
    pot1 = n1 * n1
    print(f"El número {n1} elevado al cuadrado es: {pot1}")

print("----- Cuadrados usando WHILE -----")
N2 = 1
while N2 in range(1, 61):
    POT2 = N2 * N2
    print(f"El número {N2} elevado al cuadrado es: {POT2}")
    N2 += 1
