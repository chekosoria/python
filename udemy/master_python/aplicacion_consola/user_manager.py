"""Modulo para manejar funciones relacionadas con usuarios"""
import mysql.connector
from db_settings import settings

database = mysql.connector.connect(
    host=settings.db_url,
    user=settings.db_user,
    passwd=settings.db_password,
    database=settings.db_database
)


def add_usr(usuario, password, nombre, apellido, email):
    """Función para agregar un usuario nuevo"""
    cursor = database.cursor(buffered=True)

    check_user = "select username from user where username = %s"
    cursor.execute(check_user, (usuario,))
    respuesta = cursor.fetchone()

    if respuesta is not None:
        print("El usuario ya existe")
    else:
        insert_user = """
        insert into user (username, password, nombre, apellido, email) 
        values (%s, SHA(%s), %s, %s, %s)"""
        cursor.execute(insert_user, (usuario, password,
                       nombre, apellido, email,))
        database.commit()
        print(f"El usuario {usuario} ha sido agregado")


# Probar funcion add_usr()
# add_usr('cheko', 'cheko', 'Cheko', 'Soria', 'cheko@mail.com')


def get_info(user):
    """Funcion para nombre y apellido del usuario"""
    cursor = database.cursor(buffered=True)

    # Consultamos los datos
    get_usr_info = "SELECT nombre, apellido FROM user WHERE username = %s"
    cursor.execute(get_usr_info, (user,))
    respuesta = cursor.fetchone()
    info = respuesta[0] + " " + respuesta[1]
    return info

# Para probar funcion get_info()
# print(get_info('admin'))
