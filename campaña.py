
from error import LargoExcedidoError
from anuncio import Video, Display, Social

class Campaña:
    def __init__(self, nombre, fecha_inicio, fecha_termino, datos_anuncios):
        # Validamos el nombre
        self.nombre = nombre
        self.fecha_inicio = fecha_inicio
        self.fecha_termino = fecha_termino
        # Composición: creamos internamente los objetos a partir de los datos crudos
        self.__anuncios = self.__crear_anuncios(datos_anuncios)

    # Método privado que recibe datos en diccionarios y crea instancias según tipo
    def __crear_anuncios(self, datos_anuncios):
        anuncios = []
        for dato in datos_anuncios:
            tipo = dato["tipo"]
            try:
                if tipo == "Video":
                    anuncio = Video(
                        url_archivo=dato["url_archivo"],
                        url_clic=dato["url_clic"],
                        duracion=dato["duracion"],
                        sub_tipo=dato["sub_tipo"]
                    )
                elif tipo == "Display":
                    anuncio = Display(
                        ancho=dato["ancho"],
                        alto=dato["alto"],
                        url_archivo=dato["url_archivo"],
                        url_clic=dato["url_clic"],
                        sub_tipo=dato["sub_tipo"]
                    )
                elif tipo == "Social":
                    anuncio = Social(
                        ancho=dato["ancho"],
                        alto=dato["alto"],
                        url_archivo=dato["url_archivo"],
                        url_clic=dato["url_clic"],
                        sub_tipo=dato["sub_tipo"]
                    )
                else:
                    continue  # ignoramos tipo no reconocido
                anuncios.append(anuncio)
            except Exception as e:
                print(f"Error al crear anuncio: {e}")
        return anuncios

    # Getters y setters (igual que antes)
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, value):
        if len(value) > 250:
            raise LargoExcedidoError("El nombre de la campaña excede los 250 caracteres.")
        self.__nombre = value

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

    @property
    def anuncios(self):
        return self.__anuncios

    def __str__(self):
        video_count = sum(1 for a in self.__anuncios if a.__class__.__name__ == "Video")
        display_count = sum(1 for a in self.__anuncios if a.__class__.__name__ == "Display")
        social_count = sum(1 for a in self.__anuncios if a.__class__.__name__ == "Social")
        return f"Nombre de la campaña: {self.__nombre}\nAnuncios: {video_count} Video, {display_count} Display, {social_count} Social"