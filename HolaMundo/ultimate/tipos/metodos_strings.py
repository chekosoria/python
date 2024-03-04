"""Metodos de cadenas"""
# El método upper() pasa a mayúsculas la cadena

ANIMAL = "chanchito feliz"

print(ANIMAL.upper())

# El método lower() para a minúsculas la cadena

MASCOTA = "PERRO"

print(MASCOTA.lower())

# El método capitalize() transforma la primera letra en
# mayúscula y el resto lo convierte a minúsculas

DEPREDADOR = "tiBurÓn"

print(DEPREDADOR.capitalize())

# El método title() transforma la primera letra de cada
# palabra en mayúscula y el resto lo convierte a minúsculas

CARTOON = "ratón vaQuero"

print(CARTOON.title())

# El método strip() elimina los espacios a la izquierda y derecha
# de la cadena
# también existe lstrip() para eliminar solo los espacios a la izquierda
# y rstrip() para eliminar solo los espacios a la derecha

EXTINTO = "   T-Rex  "

print(EXTINTO.strip())
print(EXTINTO.lstrip())
print(EXTINTO.rstrip())

# Es posible llamar métodos continuos como por ejemplo aplicar strip()
# y después capitalize(), solo se deben separar los métodos por un .

MITICO = "  dragón"

print(MITICO.strip().capitalize())

# El método find() permite buscar una cadena dentro de la cadena y devuelve
# índice de donde comienza la cadena buscada, para emplearlo dentro de ()
# se debe agregar como argumento la cadena a buscar
# en caso de que no se encuentre la cadena a buscar se recibe el valor -1

POKEMON = "Charizard"

print(POKEMON.find("zard"))

# El método replace() permite cambiar un o más partes de las cadenas
# para usarlo se debe mandar como argumento dentro de () la cadena a
# buscar una , y la cadena con la que se va a reemplazar
# el reemplazo es solo en la impresión y no se afecta la cadena original

FAMOSOS = "Pato Lucas"

print(FAMOSOS.replace("Lucas", "Donald"))

# Para saber si una cadena se encuentra dentro de otra se utiliza
# la cadena a buscar seguido de in seguido del nombre de la variable
# en caso de encontrar la cadena el retorno es True

print("Lucas" in FAMOSOS)

# Para saber si una cadena NO se encuentra dentro de otra se utiliza
# la cadena a buscar seguido de not in seguido del nombre de la variable
# en caso de encontrar la cadena el retorno es True

print("Donald" not in FAMOSOS)
