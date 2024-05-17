import logging


def configurar_logger():
    logging.basicConfig(
        level=logging.DEBUG,  # Puedes cambiar el nivel de log aquí
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler("app.log"),  # Guarda los logs en un archivo
            logging.StreamHandler()  # Muestra los logs en la consola
        ]
    )
    logger = logging.getLogger(__name__)
    return logger
