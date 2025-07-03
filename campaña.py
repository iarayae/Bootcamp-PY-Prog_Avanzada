from error import LargoExcedidoError

# Definición de la clase Campaña
class Campaña:
    def __init__(self, nombre, fecha_inicio, fecha_termino, anuncios):
        # Atributos de instancia privados (se aplicará encapsulamiento más adelante)
        self.nombre = nombre  # usa setter para validación
        self.fecha_inicio = fecha_inicio
        self.fecha_termino = fecha_termino
        self.__anuncios = anuncios  # solo getter, no setter

    # Getter y setter para nombre (valida largo)
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, value):
        if len(value) > 250:
            raise LargoExcedidoError("El nombre de la campaña excede los 250 caracteres.")
        self.__nombre = value

    # Setters simples para fechas (no hay validación solicitada)
    @property
    def fecha_inicio(self):
        return self.__fecha_inicio

    @fecha_inicio.setter
    def fecha_inicio(self, value):
        self.__fecha_inicio = value

    @property
    def fecha_termino(self):
        return self.__fecha_termino

    @fecha_termino.setter
    def fecha_termino(self, value):
        self.__fecha_termino = value

    # Getter único para anuncios (sin setter)
    @property
    def anuncios(self):
        return self.__anuncios

    def __str__(self):
        # Contamos cuántos anuncios hay de cada tipo
        video_count = sum(1 for a in self.__anuncios if a.__class__.__name__ == "Video")
        display_count = sum(1 for a in self.__anuncios if a.__class__.__name__ == "Display")
        social_count = sum(1 for a in self.__anuncios if a.__class__.__name__ == "Social")

        # Retornamos una cadena con los datos solicitados
        return f"Nombre de la campaña: {self.__nombre}\nAnuncios: {video_count} Video, {display_count} Display, {social_count} Social"