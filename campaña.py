# Definición inicial de la clase Campaña

# Por ahora solo se declara la estructura básica
class Campaña:
    def __init__(self, nombre, fecha_inicio, fecha_termino, anuncios):
        # Atributos de instancia privados (se aplicará encapsulamiento más adelante)
        self.__nombre = nombre
        self.__fecha_inicio = fecha_inicio
        self.__fecha_termino = fecha_termino
        self.__anuncios = anuncios  # Lista de objetos: Video, Display, Social

    def __str__(self):
        # Contamos cuántos anuncios hay de cada tipo
        video_count = sum(1 for a in self.__anuncios if a.__class__.__name__ == "Video")
        display_count = sum(1 for a in self.__anuncios if a.__class__.__name__ == "Display")
        social_count = sum(1 for a in self.__anuncios if a.__class__.__name__ == "Social")

        # Retornamos una cadena con los datos solicitados
        return f"Nombre de la campaña: {self.__nombre}\nAnuncios: {video_count} Video, {display_count} Display, {social_count} Social"