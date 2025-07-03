from abc import ABC, abstractmethod
from error import SubTipoInvalidoError

# Clase base Anuncio
# Servirá como clase padre para los tipos específicos de anuncios
class Anuncio(ABC):
    def __init__(self, ancho, alto, url_archivo, url_clic, sub_tipo):
        # Asignamos ancho y alto con setter para aplicar validaciones
        self.ancho = ancho
        self.alto = alto
        self.url_archivo = url_archivo
        self.url_clic = url_clic
        self.sub_tipo = sub_tipo  # validado en setter

    # Getters y setters con encapsulamiento y reglas
    @property
    def ancho(self):
        return self.__ancho

    @ancho.setter
    def ancho(self, value):
        self.__ancho = value if value > 0 else 1

    @property
    def alto(self):
        return self.__alto

    @alto.setter
    def alto(self, value):
        self.__alto = value if value > 0 else 1

    @property
    def sub_tipo(self):
        return self.__sub_tipo

    @sub_tipo.setter
    def sub_tipo(self, value):
        # Validamos si el subtipo está dentro de los permitidos según la clase hija
        if value not in self.__class__.SUB_TIPOS:
            raise SubTipoInvalidoError(f"Subtipo inválido para {self.__class__.__name__}: {value}")
        self.__sub_tipo = value

    @property
    def url_archivo(self):
        return self.__url_archivo

    @url_archivo.setter
    def url_archivo(self, value):
        self.__url_archivo = value

    @property
    def url_clic(self):
        return self.__url_clic

    @url_clic.setter
    def url_clic(self, value):
        self.__url_clic = value

    # Métodos abstractos obligatorios en subclases
    @abstractmethod
    def comprimir_anuncio(self):
        pass

    @abstractmethod
    def redimensionar_anuncio(self):
        pass


# Clase Video que hereda de Anuncio
# Define atributos de clase especificos para el tipo de anuncio "Video"
class Video(Anuncio):
    FORMATO = "Video" # Tipo de formato
    SUB_TIPOS = ("instream", "outstream") # subtipos válidos para anuncios en video

    def __init__(self, url_archivo, url_clic, duracion, sub_tipo):
        # Llama al constructor de la clase padre con valores fijos (ancho=1, alto=1)
        super().__init__(1, 1, url_archivo, url_clic, sub_tipo)
        # Duración personalizada para videos
        self.duracion = duracion
    
    @property
    def duracion(self):
        return self.__duracion

    @duracion.setter
    def duracion(self, value):
        self.__duracion = value if value > 0 else 5

    def comprimir_anuncio(self):
        print("COMPRESIÓN DE VIDEO NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        print("RECORTE DE VIDEO NO IMPLEMENTADO AÚN")


# Clase Display que hereda tambien de Anuncio
# Define atributos de clase especificos para el tipo de anuncio "Display"
class Display(Anuncio):
    FORMATO = "Display" # Tipo de Formato
    SUB_TIPOS = ("tradicional", "native") # subtipos validos para este tipo de anuncio

    def __init__(self, ancho, alto, url_archivo, url_clic, sub_tipo):
        # Constructor con valores personalizados
        super().__init__(ancho, alto, url_archivo, url_clic, sub_tipo)

    def comprimir_anuncio(self):
        print("COMPRESIÓN DE ANUNCIOS DISPLAY NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        print("REDIMENSIONAMIENTO DE ANUNCIOS DISPLAY NO IMPLEMENTADO AÚN")


# Clase Social que hereda de Anuncio
# Define atributos de clase especificos para el tipo de anuncio en redes sociales
class Social(Anuncio):
    FORMATO = "Social"
    SUB_TIPOS = ("facebook", "linkedin")

    def __init__(self, ancho, alto, url_archivo, url_clic, sub_tipo):
        # Constructor con valores personalizados
        super().__init__(ancho, alto, url_archivo, url_clic, sub_tipo)
    
    def comprimir_anuncio(self):
        print("COMPRESIÓN DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        print("REDIMENSIONAMIENTO DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADO AÚN")