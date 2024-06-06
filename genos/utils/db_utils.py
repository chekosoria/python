"""Utilería para establecer conexión con base de datos local"""
import sqlite3
import os


def obtener_ruta_db():
    """Obtener la ruta completa del archivo de base de datos"""
    current_directory = os.path.dirname(os.path.realpath(__file__))
    db_path = os.path.join(current_directory, "../endpoints.db")
    return db_path


def inicializar_base_de_datos():
    """Inicializar la base de datos y crear la tabla de endpoints si no existe"""
    db_path = obtener_ruta_db()
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        # Tabla para anexos por lote
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS anexos_lote (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                alias TEXT NOT NULL,
                url TEXT NOT NULL,
                parametros TEXT NOT NULL,
                download_url TEXT NOT NULL,
                ambiente TEXT NOT NULL
            )
        """)
        conn.commit()
        # Tabla para anexos individuales
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS anexos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                alias TEXT NOT NULL,
                url TEXT NOT NULL,
                parametros TEXT NOT NULL,
                download_url TEXT NOT NULL,
                ambiente TEXT NOT NULL
            )
        """)
        conn.commit()
        # Tabla para otros reportes
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS endpoints (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                alias TEXT NOT NULL,
                url TEXT NOT NULL,
                parametros TEXT NOT NULL,
                download_url TEXT NOT NULL,
                ambiente TEXT NOT NULL
            )
        """)
        conn.commit()


def obtener_conexion():
    """Obtener una conexión a la base de datos"""
    db_path = obtener_ruta_db()
    return sqlite3.connect(db_path)
