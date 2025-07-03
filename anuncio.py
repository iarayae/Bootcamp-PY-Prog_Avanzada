# Clase base Anuncio
# Servirá como clase padre para los tipos específicos de anuncios
class Anuncio:
    def __init__(self, ancho, alto, url_archivo, url_clic, sub_tipo):
        # Asignación básica de atributos, se completará con validaciones más adelante
        self.__ancho = ancho
        self.__alto = alto
        self.__url_archivo = url_archivo
        self.__url_clic = url_clic
        self.__sub_tipo = sub_tipo


# Clase Video que hereda de Anuncio
# Define atributos de clase especificos para el tipo de anuncio "Video"
class Video(Anuncio):
    FORMATO = "Video" # Tipo de formato
    SUB_TIPOS = ("instream", "outstream") # subtipos válidos para anuncios en video

    def __init__(self, url_archivo, url_clic, duracion, sub_tipo):
        # Llama al constructor de la clase padre con valores fijos (ancho=1, alto=1)
        super().__init__(1, 1, url_archivo, url_clic, sub_tipo)
        # Duración personalizada para videos
        self.__duracion = duracion


# Clase Display que hereda tambien de Anuncio
# Define atributos de clase especificos para el tipo de anuncio "Display"
class Display(Anuncio):
    FORMATO = "Display" # Tipo de Formato
    SUB_TIPOS = ("tradicional", "native") # subtipos validos para este tipo de anuncio

    def __init__(self, ancho, alto, url_archivo, url_clic, sub_tipo):
        # Constructor con valores personalizados
        super().__init__(ancho, alto, url_archivo, url_clic, sub_tipo)


# Clase Social que hereda de Anuncio
# Define atributos de clase especificos para el tipo de anuncio en redes sociales
class Social(Anuncio):
    FORMATO = "Social"
    SUB_TIPOS = ("facebook", "linkedin")

    def __init__(self, ancho, alto, url_archivo, url_clic, sub_tipo):
        # Constructor con valores personalizados
        super().__init__(ancho, alto, url_archivo, url_clic, sub_tipo)