"""Grupos en Python"""

# Es una especia de lista pero evita repeticiones
# se define como una lista pero los valores se agregan
# dentro de {}
# primer = {1, 1, 2, 2, 3, 4}

primer = [1, 1, 2, 2, 3, 4]

primer = set(primer)

print(primer)

segundo = [3, 4, 5]

segundo = set(segundo)

print(segundo)

# Para juntar dos o más sets |

print(primer | segundo)

# Para obtener la intersección de dos sets &

print(primer & segundo)

# Para obtener la diferencia entre dos sets -
# se muestran los datos que están en el set
# de la izquierda quitando lo que se encuentran
# también en el de la derecha

print(primer - segundo)

# La diferencia simetrica ^ (alt + 94)
# devuelve los elementos de ambos sets
# que no se encuentren en ambos

print(primer ^ segundo)
