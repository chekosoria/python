"""Ejercicios funciones"""


def es_palindromo(texto):
    """Función para evaluar cadena de texto si es palindromo"""
    palabra = texto.replace(" ", "")
    if palabra == "".join(reversed(palabra)):
        return True
    return False


word = input("Ingrese una palabra o frase: ")

print(f"{word}, {es_palindromo(word.lower())}")
