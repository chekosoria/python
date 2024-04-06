"""
Proytecto dia 6. Rehacer la calculadora usando funciones.
- Usar ciclo while para que el usuario tenga el control de cuando salir
de la calculadora
"""


def get_suma(a, b):
    """Función para obtener la suma de 2 números"""
    return a + b


def get_resta(a, b):
    """Función para obtener la resta de 2 números"""
    return a - b


def get_multiplicacion(a, b):
    """Función para obtener la multiplicación de 2 números"""
    return a * b


def get_division(a, b):
    """Función para obtener la división de 2 números"""
    return a / b


def get_modulo(a, b):
    """Función para obtener el módulo de 2 números"""
    return a % b


def get_exponente(a, b):
    """Función para obtener el exponente de 1 número elevado a otro número"""
    return a ** b


while True:
    print("---------- Calculadora básica ----------")
    print("Para suma ingrese ...................(1)")
    print("Para resta ingrese ..................(2)")
    print("Para multiplicación ingrese .........(3)")
    print("Para división ingrese ...............(4)")
    print("Para módulo ingrese .................(5)")
    print("Para exponente ingrese ..............(6)")
    print("Para salir ingrese ..................(7)")
    print("----------------------------------------")

    opcion = int(input("Opción: "))

    match opcion:
        case 1:
            print("\n--- Ha seleccionado suma ---\n")
        case 2:
            print("\n--- Ha seleccionado resta ---\n")
        case 3:
            print("\n--- Ha seleccionado multiplicación ---\n")
        case 4:
            print("\n--- Ha seleccionado división ---\n")
        case 5:
            print("\n--- Ha seleccionado módulo ---\n")
        case 6:
            print("\n--- Ha seleccionado exponente ---\n")
        case 7:
            print("\n--- Ha seleccionado salir ---\n")
            print("\nAdios\n")
            break
        case _:
            print("\nOpción no soportada\n")
            break

    numero1 = int(input("Ingrese primer número: \n"))
    numero2 = int(input("Ingrese segundo número: \n"))

    match opcion:
        case 1:
            suma = get_suma(numero1, numero2)
            print(f"El resultado de la suma es {suma}\n\n")
        case 2:
            resta = get_resta(numero1, numero2)
            print(f"El resultado de la resta es {resta}\n\n")
        case 3:
            multiplicacion = get_multiplicacion(numero1, numero2)
            print(f"El resultado de la multiplicación es {multiplicacion}\n\n")
        case 4:
            if numero2 == 0:
                print("No se puede dividir entre 0\n\n")
            elif numero1 == 0:
                print("No se puede dividir 0 entre algo\n\n")
            elif numero1 > numero2:
                division = get_division(numero1, numero2)
                print(f"El resultado de la división es {division}\n\n")
        case 5:
            if numero2 == 0:
                print("No se puede dividir entre 0\n\n")
            elif numero1 == 0:
                print("No se puede dividir 0 entre algo\n\n")
            elif numero1 > numero2:
                modulo = get_modulo(numero1, numero2)
                print(f"El módulo es {modulo}\n\n")
        case 6:
            if numero1 == 0:
                print(f"El resultado de elevar {
                    numero1} a la {numero2} es 0\n\n")
            elif numero2 == 0:
                print(f"El resultado de elevar {
                    numero1} a la {numero2} es 1\n\n")
            else:
                exponente = get_exponente(numero1, numero2)
                print(f"El resultado de elevar {
                    numero1} a la {numero2} es {exponente}\n\n")
