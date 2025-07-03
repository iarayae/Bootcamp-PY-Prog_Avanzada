from campaña import Campaña
from error import Error
import sys

# Creamos una campaña inicial con un anuncio de tipo Video
datos = [
    {
        "tipo": "Video",
        "url_archivo": "video1.mp4",
        "url_clic": "https://example.com",
        "duracion": 10,
        "sub_tipo": "instream"
    }
]

campaña = Campaña("Campaña Prueba", "2025-07-01", "2025-07-31", datos)

# Intentamos modificar los atributos con entrada del usuario
try:
    nuevo_nombre = input("Ingrese nuevo nombre de la campaña: ")
    campaña.nombre = nuevo_nombre

    nuevo_subtipo = input("Ingrese nuevo subtipo para el anuncio: ")
    campaña.anuncios[0].sub_tipo = nuevo_subtipo

except Error as e:
    print(f"Ocurrió una excepción: {e}")
    # Guardamos el mensaje en el archivo error.log
    with open("error.log", "a", encoding="utf-8") as log:
        log.write(str(e) + "\n")