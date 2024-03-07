"""Calculadora mejorada"""

print("--------------------------------")
print("| Bienvenidos a la calculadora |")
print("--------------------------------")
print("|                              |")
print("| Opciones disponibles:        |")
print("|                              |")
print("| Suma                      (s)|")
print("| Resta                     (r)|")
print("| Multiplicación            (m)|")
print("| Divisón                   (d)|")
print("| Salir                 (salir)|")
print("|                              |")
print("--------------------------------")

RESULTADO = ""

while True:
    if not RESULTADO:
        RESULTADO = input("Ingrese número:  ")
        if RESULTADO.lower() == "salir":
            break
        RESULTADO = int(RESULTADO)
    OP = input("Ingresa operación: ")
    if OP.lower() == "salir":
        break
    N2 = input("Ingrese siguiente número: ")
    if N2.lower() == "salir":
        break
    N2 = int(N2)

    if OP.lower() == "s":
        RESULTADO += N2

    elif OP.lower() == "r":
        RESULTADO -= N2

    elif OP.lower() == "m":
        RESULTADO *= N2

    elif OP.lower() == "d":
        RESULTADO /= N2

    else:
        print("Operación no válida")
        break

    print(f"El resultado es {RESULTADO}")
