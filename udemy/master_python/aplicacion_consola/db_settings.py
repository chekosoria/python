"""Database settings"""
import os
from dataclasses import dataclass
from dotenv import load_dotenv


@dataclass
class Settings:
    """Clase para cargar configuracion de DB desde .env"""
    db_url: str
    db_user: str
    db_password: str
    db_database: str


load_dotenv()

DB_URL = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_DATABASE = os.getenv("DB_DATABASE")


settings = Settings(db_url=DB_URL, db_user=DB_USER,
                    db_password=DB_PASSWORD, db_database=DB_DATABASE)
