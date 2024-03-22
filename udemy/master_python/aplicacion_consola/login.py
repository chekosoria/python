"""Modulo Login"""
import hashlib
import mysql.connector
from db_settings import settings

database = mysql.connector.connect(
    host=settings.db_url,
    user=settings.db_user,
    passwd=settings.db_password,
    database=settings.db_database
)


def autenticar(user, password):
    """Funcion para obtener password desde DB y compararla de manera segura"""
    cursor = database.cursor(buffered=True)

    # Consultamos el password
    get_password = "SELECT password FROM user WHERE username = %s"
    cursor.execute(get_password, (user,))
    respuesta = cursor.fetchone()

    # Para depurar
    # print("Respuesta de la consulta:", respuesta)

    if respuesta:
        # Obtenemos el hash SHA de la contraseña ingresada
        password_hash = hashlib.sha1(password.encode()).hexdigest()

        # Para depurar
        # print("Contraseña hash generada:", password_hash)
        # print("Contraseña almacenada en la base de datos:", respuesta[0])

        if password_hash == respuesta[0]:
            return True
    return False
