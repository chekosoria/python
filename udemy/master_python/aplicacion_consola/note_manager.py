"""Modulo para manejar funcionalidades relacionadas con las notas"""
import mysql.connector
from db_settings import settings

database = mysql.connector.connect(
    host=settings.db_url,
    user=settings.db_user,
    passwd=settings.db_password,
    database=settings.db_database
)


def agregar_nota(usuario, mensaje):
    """Función para agregar nueva nota"""
    cursor = database.cursor(buffered=True)

    get_user_id = "select id from user where username = %s"
    cursor.execute(get_user_id, (usuario,))
    respuesta = cursor.fetchone()

    if respuesta:
        user_id = respuesta[0]
        insert_note = "insert into notas (creator, texto) values (%s, %s)"
        cursor.execute(insert_note, (user_id, mensaje,))
        database.commit()
        print("La nota ha sido agregada")
    else:
        print("Error al agregar nota, usuario no encontrado")


# Para probar función agregar_nota()
# agregar_nota('admin', 'Hola mundo')


def consultar_nota(usuario):
    """Función para mostrar notas del usuario actual"""
    cursor = database.cursor(buffered=True)

    get_user_id = "select id from user where username = %s"
    cursor.execute(get_user_id, (usuario,))
    respuesta = cursor.fetchone()

    if respuesta:
        user_id = respuesta[0]
        get_notes = "select id, texto from notas where creator = %s"
        cursor.execute(get_notes, (user_id,))
        for identificador, texto in cursor:
            print(f"ID de la nota: {
                  identificador}\nTexto de la nota: {texto}\n")
    else:
        print("Sin mensajes")

# Para probar función consultar_nota()
# consultar_nota('admin')


def borrar_nota(id_nota):
    """Función para borrar nota por ID"""
    cursor = database.cursor(buffered=True)

    get_note_by_id = "select id from notas where id = %s"
    cursor.execute(get_note_by_id, (id_nota,))
    respuesta = cursor.fetchone()

    if respuesta:
        delete_note = "delete from notas where id = %s"
        cursor.execute(delete_note, (id_nota,))
        database.commit()
        print("Se ha eliminado la nota solicitada")
    else:
        print("No se encuentra la nota solicitada")


# Probar funcion borrar_nota()
# borrar_nota(3)


def borrar_notas(usuario):
    """Función para borrar todas las notas de un usuario"""
    cursor = database.cursor(buffered=True)

    get_user_id = "select id from user where username = %s"
    cursor.execute(get_user_id, (usuario,))
    respuesta = cursor.fetchone()

    user_id = respuesta[0]

    get_note_by_user = "select id from notas where creator = %s"
    cursor.execute(get_note_by_user, (user_id,))
    respuesta = cursor.fetchone()

    if respuesta:
        delete_notes = "delete from notas where creator = %s"
        cursor.execute(delete_notes, (user_id,))
        database.commit()
        print("Se han eliminado las notas solicitadas")
    else:
        print("No se encuentran notas para el usuario actual")


# Probar funcion borrar_notas()
# borrar_notas('admin')
