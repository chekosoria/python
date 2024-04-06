"""
Proyecto día 3. Hacer una calculadora que pida al usuario dos números y de la opción
de obtener suma, resta, multiplicación, módulo y exponente
"""
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

ERROR = True

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
        ERROR = False
    case _:
        print("\nOpción no soportada\n")
        ERROR = False

if ERROR:
    numero1 = int(input("Ingrese primer número: \n"))
    numero2 = int(input("Ingrese segundo número: \n"))

    match opcion:
        case 1:
            suma = numero1 + numero2
            print(f"El resultado de la suma es {suma}")
        case 2:
            resta = numero1 - numero2
            print(f"El resultado de la resta es {resta}")
        case 3:
            multiplica = numero1 * numero2
            print(f"El resultado de la multiplicación es {multiplica}")
        case 4:
            if numero2 == 0:
                print("No se puede dividir entre 0")
            elif numero1 == 0:
                print("No se puede dividir 0 entre algo")
            elif numero1 > numero2:
                division = numero1 / numero2
                print(f"El resultado de la división es {division}")
        case 5:
            if numero2 == 0:
                print("No se puede dividir entre 0")
            elif numero1 == 0:
                print("No se puede dividir 0 entre algo")
            elif numero1 > numero2:
                modulo = numero1 % numero2
                print(f"El módulo es {modulo}")
        case 6:
            if numero1 == 0:
                print(f"El resultado de elevar {
                    numero1} a la {numero2} es 0")
            elif numero2 == 0:
                print(f"El resultado de elevar {
                    numero1} a la {numero2} es 1")
            else:
                exponente = numero1 ** numero2
                print(f"El resultado de elevar {
                    numero1} a la {numero2} es {exponente}")
else:
    print("Saliendo de la calculadora....")
