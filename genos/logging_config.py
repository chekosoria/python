"""Módulo para configurar el log en general de la aplicación"""
import logging

SISTEMA = "Genos"


def configurar_logger():
    """Método para configurar el log"""
    logging.basicConfig(
        level=logging.INFO,  # Puedes cambiar el nivel de log aquí
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            # Guarda los logs en un archivo
            logging.FileHandler(f"{SISTEMA.lower()}.log"),
            logging.StreamHandler()  # Muestra los logs en la consola
        ]
    )
    logger = logging.getLogger(__name__)
    return logger
