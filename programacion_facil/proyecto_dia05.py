"""
Proyecto día 5.
- Añade un título con un print para la pizzeria
- El usuario debe introducir el dinero que quiera gastar, el dato se debe 
guardar en una variable
- Usando una lista añade los ingredientes extra usando los métodos de adición en listas
- Deben existir un mínimo de tres tipos de pizzas para poder elegir
- Cada pizza debe tener un precio diferente
- El usuario podrá elegir solo una pizza
- Se debe ir informando al usuario el total de su compra tras cada movimiento
- Se debe preguntar si el usuario desea ingredientes extra los cuales se cobran aparte
- En las pruebas se deben agregar por lo menos tres ingredientes extras, el usuario debe
ser capaz de agregar los que quiera
- Si después de sumar el costo inicial de la pizza más los ingredientes extra se pasa del 
presupuesto inicial se debe avisar al usuario y se debe iniciar nuevamente el pedido
- Las pizzas e ingredientes deben tener sus precios almacenados en variables
- Al agregar ingredientes extra se debe mostrar el balance al usuario 
(presupuesto inicial - compra total)
"""
print("---------- Bienvenido a Pizzeria Panuchi ----------")
print("|                                                 |")
print("| Por favor ingrese dinero a su cuenta            |")
print("|                                                 |")
print("---------------------------------------------------")
dinero = float(input("Ingrese la cantidad de dinero deseada $"))

SALDO = dinero
VENTA_TOTAL = 0.0

# Pizzas
QUESO = 90.0
PEPERONI = 95.0
HAWAIANA = 120.0
CARNES = 150.0
VEGETARIANA = 110.0

# Extras
SALSA = 10.0
CEBOLLA = 5.0
QSO = 15.0
CHAMPI = 20.0
PPRONI = 16.0
JAMON = 9.0
PINA = 7.0
KRNE = 30.0

pedido = []

while True:
    print("\n\n\n\n")
    print("---------- Bienvenido a Pizzeria Panuchi ----------")
    print("|                                                 |")
    print("| Indique la pizza que desea ordenar:             |")
    print("|                               PRECIO            |")
    print(f"| Queso .......................${round(QUESO, 2)}...........(1)|")
    print(f"| Peperoni ....................${
          round(PEPERONI, 2)}...........(2)|")
    print(f"| Hawaiana ....................${
          round(HAWAIANA, 2)}..........(3)|")
    print(f"| Carnes ......................${round(CARNES, 2)}..........(4)|")
    print(f"| Vegetariana .................${
          round(VEGETARIANA, 2)}..........(5)|")
    print("| Salir .......................................(6)|")
    print("|                                                 |")
    print("---------------------------------------------------")
    opcion = int(input("Opción: "))

    match opcion:
        case 1:
            if dinero < QUESO:
                print("Saldo insuficiente...")
            else:
                print(f"Ha elegido la pizza de Queso\n Venta total ${
                      round(QUESO, 2)}")
                dinero -= QUESO
                print(f"Le queda un saldo de ${round(dinero, 2)}")
                VENTA_TOTAL += QUESO
                pedido.append(f"Pizza de Queso           ${round(QUESO, 2)}")
                break
        case 2:
            if dinero < PEPERONI:
                print("Saldo insuficiente...")
            else:
                print(
                    f"Ha elegido la pizza de Peperoni\n Venta total ${round(PEPERONI, 2)}")
                dinero -= PEPERONI
                print(f"Le queda un saldo de ${round(dinero, 2)}")
                VENTA_TOTAL += PEPERONI
                pedido.append(f"Pizza de Peperoni        ${
                              round(PEPERONI, 2)}")
                break
        case 3:
            if dinero < HAWAIANA:
                print("Saldo insuficiente...")
            else:
                print(
                    f"Ha elegido la pizza de Hawaiana\n Venta total ${round(HAWAIANA, 2)}")
                dinero -= HAWAIANA
                print(f"Le queda un saldo de ${round(dinero, 2)}")
                VENTA_TOTAL += HAWAIANA
                pedido.append(f"Pizza de Hawaiana        ${
                              round(HAWAIANA, 2)}")
                break
        case 4:
            if dinero < CARNES:
                print("Saldo insuficiente...")
            else:
                print(f"Ha elegido la pizza de Carnes\n Venta total ${
                      round(CARNES, 2)}")
                dinero -= CARNES
                print(f"Le queda un saldo de ${round(dinero, 2)}")
                VENTA_TOTAL += CARNES
                pedido.append(f"Pizza de Carnes          ${round(CARNES, 2)}")
                break
        case 5:
            if dinero < VEGETARIANA:
                print("Saldo insuficiente...")
            else:
                print(f"Ha elegido la pizza Vegetariana\n Venta total ${
                      round(VEGETARIANA, 2)}")
                dinero -= VEGETARIANA
                print(f"Le queda un saldo de ${round(dinero, 2)}")
                VENTA_TOTAL += VEGETARIANA
                pedido.append(f"Pizza Vegetariana        ${
                              round(VEGETARIANA, 2)}")
                break
        case 6:
            break
        case _:
            print("Opción no disponible, ingrese una opción valida")

while True:
    print("\n\n\n\n")
    print("------- Desea agregar un ingrediente extra? -------")
    print("|                                                 |")
    print("| Si ..........................................(1)|")
    print("| No ..........................................(2)|")
    print("|                                                 |")
    print("---------------------------------------------------")
    opcion_extra = int(input("Opción: "))

    match opcion_extra:
        case 1:
            while True:
                print("\n\n\n\n")
                print("--------------- Ingredientes  extra ---------------")
                print("|                                                 |")
                print(f"| Salsa .......................${
                      round(SALSA, 2)}...........(1)|")
                print(f"| Cebolla .....................${
                      round(CEBOLLA, 2)}............(2)|")
                print(f"| Queso .......................${QSO}...........(3)|")
                print(f"| Champiñones .................${
                      round(CHAMPI, 2)}...........(4)|")
                print(f"| Peperoni ....................${
                      round(PPRONI, 2)}...........(5)|")
                print(f"| Jamón .......................${
                      round(JAMON, 2)}............(6)|")
                print(f"| Piña ........................${
                      round(PINA, 2)}............(7)|")
                print(f"| Carne Molida ................${
                      round(KRNE, 2)}...........(8)|")
                print("| Salir .......................................(9)|")
                print("|                                                 |")
                print("---------------------------------------------------")
                extra = int(input("Opción: "))

                match extra:
                    case 1:
                        if dinero < SALSA:
                            print("Saldo insuficiente...")
                        else:
                            print(
                                f"Ha elegido agregar Salsa extra \n Por ${round(SALSA, 2)} extras")
                            dinero -= SALSA
                            print(f"Le queda un saldo de ${round(dinero, 2)}")
                            VENTA_TOTAL += SALSA
                            pedido.append(f"Salsa extra              ${
                                          round(SALSA, 2)}")
                    case 2:
                        if dinero < CEBOLLA:
                            print("Saldo insuficiente...")
                        else:
                            print(
                                f"Ha elegido agregar Cebolla extra \n Por ${
                                    round(CEBOLLA, 2)} adicionales")
                            dinero -= CEBOLLA
                            print(f"Le queda un saldo de ${round(dinero, 2)}")
                            VENTA_TOTAL += CEBOLLA
                            pedido.append(
                                f"Cebolla extra            ${round(CEBOLLA, 2)}")
                    case 3:
                        if dinero < QSO:
                            print("Saldo insuficiente...")
                        else:
                            print(
                                f"Ha elegido agregar Queso extra \n Por ${
                                    round(QSO, 2)} adicionales")
                            dinero -= QSO
                            print(f"Le queda un saldo de ${round(dinero, 2)}")
                            VENTA_TOTAL += QSO
                            pedido.append(f"Queso extra              ${
                                          round(QSO, 2)}")
                    case 4:
                        if dinero < CHAMPI:
                            print("Saldo insuficiente...")
                        else:
                            print(
                                f"Ha elegido agregar Champiñones extra \n Por ${
                                    round(CHAMPI, 2)} adicionales")
                            dinero -= CHAMPI
                            print(f"Le queda un saldo de ${round(dinero, 2)}")
                            VENTA_TOTAL += CHAMPI
                            pedido.append(
                                f"Champiñones extra        ${round(CHAMPI, 2)}")
                    case 5:
                        if dinero < PPRONI:
                            print("Saldo insuficiente...")
                        else:
                            print(
                                f"Ha elegido agregar Peperoni extra \n Por ${
                                    round(PPRONI, 2)} adicionales")
                            dinero -= PPRONI
                            print(f"Le queda un saldo de ${round(dinero, 2)}")
                            VENTA_TOTAL += PPRONI
                            pedido.append(
                                f"Peperoni extra           ${round(PPRONI, 2)}")
                    case 6:
                        if dinero < JAMON:
                            print("Saldo insuficiente...")
                        else:
                            print(
                                f"Ha elegido agregar Jamón extra \n Por ${
                                    round(JAMON, 2)} adicionales")
                            dinero -= JAMON
                            print(f"Le queda un saldo de ${round(dinero, 2)}")
                            VENTA_TOTAL += JAMON
                            pedido.append(f"Jamón extra              ${
                                          round(JAMON, 2)}")
                    case 7:
                        if dinero < PINA:
                            print("Saldo insuficiente...")
                        else:
                            print(
                                f"Ha elegido agregar Piña extra \n Por ${
                                    round(PINA, 2)} adicionales")
                            dinero -= PINA
                            print(f"Le queda un saldo de ${round(dinero, 2)}")
                            VENTA_TOTAL += PINA
                            pedido.append(f"Piña extra               ${
                                          round(PINA, 2)}")
                    case 8:
                        if dinero < KRNE:
                            print("Saldo insuficiente...")
                        else:
                            print(
                                f"Ha elegido agregar Carne Molida extra \n Por ${
                                    round(KRNE, 2)} adicionales")
                            dinero -= KRNE
                            print(f"Le queda un saldo de ${round(dinero, 2)}")
                            VENTA_TOTAL += KRNE
                            pedido.append(f"Carne Molida extra       ${
                                          round(KRNE, 2)}")
                    case 9:
                        break
                    case _:
                        print("Opción no disponible, ingrese una opción valida")

        case 2:
            break
        case _:
            print("Opción no disponible, ingrese una opción valida")


print(f"Su saldo actual es {round(dinero, 2)}")

print("\nImprimiendo recibo................\n")

for elemento in pedido:
    print(elemento)
print(f"Venta total .............${round(VENTA_TOTAL, 2)}")
