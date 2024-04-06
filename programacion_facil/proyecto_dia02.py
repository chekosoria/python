"""
Proyecto día 2. Hacer una calculadora sencilla de exponentes, esta calculadora
deberá pedir al usuario los números que quiere (base y exponente)
"""
print(" -- Calculadora de exponente -- \n")
base = int(input("Ingrese el numero base: \n"))
exponente = int(input("Ingrese el exponente: \n"))
resultado = base ** exponente

print(f"El resultado de elevar {base} a la {exponente} es {resultado}")
