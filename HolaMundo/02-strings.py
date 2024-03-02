# Definición de variable tipo cadena
texto = "Hola Mundo"
# Imprimir el texto en mayúsculas
print(texto.upper())
# Imprimir el texto en minúsculas
print(texto.lower())
# Busca el índice del caracter deseado
print(texto.find("M"))
# Reemplaza la cadena original (temporalmente)
print(texto.replace("Hola Mundo", "Hello World"))
# Asigna a una variable el reemplazo de la cadena original
nuevoTexto = texto.replace("Hola Mundo", "Hello World")
# Imprime las 2 variables
print(texto, nuevoTexto)
# Indica si la cadena buscada se encuentra en la variable
print("Mundo" in texto)