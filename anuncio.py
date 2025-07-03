from abc import ABC, abstractmethod
from error import SubTipoInvalidoError

# Clase abstracta base para todos los tipos de anuncios
class Anuncio(ABC):
    def __init__(self, ancho, alto, url_archivo, url_clic, sub_tipo):
        # Se asignan los atributos usando los setters con validación
        self.ancho = ancho
        self.alto = alto
        self.url_archivo = url_archivo
        self.url_clic = url_clic
        self.sub_tipo = sub_tipo

    # Getter y setter para ancho, asegura que sea mayor a cero
    @property
    def ancho(self):
        return self.__ancho

    @ancho.setter
    def ancho(self, value):
        self.__ancho = value if value > 0 else 1

    # Getter y setter para alto, asegura que sea mayor a cero
    @property
    def alto(self):
        return self.__alto

    @alto.setter
    def alto(self, value):
        self.__alto = value if value > 0 else 1

    # Getter y setter para url del archivo del anuncio
    @property
    def url_archivo(self):
        return self.__url_archivo

    @url_archivo.setter
    def url_archivo(self, value):
        self.__url_archivo = value

    # Getter y setter para url de redirección al hacer clic
    @property
    def url_clic(self):
        return self.__url_clic

    @url_clic.setter
    def url_clic(self, value):
        self.__url_clic = value

    # Getter y setter para subtipo, validando con SUB_TIPOS de la subclase
    @property
    def sub_tipo(self):
        return self.__sub_tipo

    @sub_tipo.setter
    def sub_tipo(self, value):
        if value not in self.__class__.SUB_TIPOS:
            raise SubTipoInvalidoError(f"Subtipo inválido para {self.__class__.__name__}: {value}")
        self.__sub_tipo = value

    # Métodos abstractos que deben implementar las subclases
    @abstractmethod
    def comprimir_anuncio(self):
        pass

    @abstractmethod
    def redimensionar_anuncio(self):
        pass

    # Método de colaboración: muestra los formatos y subtipos disponibles
    @staticmethod
    def mostrar_formatos():
        for clase in [Video, Display, Social]:
            print(f"FORMATO: {clase.FORMATO}")
            for subtipo in clase.SUB_TIPOS:
                print(f"- {subtipo}")
            print()


# Clase Video que hereda de Anuncio
class Video(Anuncio):
    FORMATO = "Video"
    SUB_TIPOS = ("instream", "outstream")

    def __init__(self, url_archivo, url_clic, duracion, sub_tipo):
        # Video tiene tamaño fijo: 1x1
        super().__init__(1, 1, url_archivo, url_clic, sub_tipo)
        self.duracion = duracion  # usa setter

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


# Clase Display que hereda de Anuncio
class Display(Anuncio):
    FORMATO = "Display"
    SUB_TIPOS = ("traditional", "native")

    def __init__(self, ancho, alto, url_archivo, url_clic, sub_tipo):
        super().__init__(ancho, alto, url_archivo, url_clic, sub_tipo)

    def comprimir_anuncio(self):
        print("COMPRESIÓN DE ANUNCIOS DISPLAY NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        print("REDIMENSIONAMIENTO DE ANUNCIOS DISPLAY NO IMPLEMENTADO AÚN")


# Clase Social que hereda de Anuncio
class Social(Anuncio):
    FORMATO = "Social"
    SUB_TIPOS = ("facebook", "linkedin")

    def __init__(self, ancho, alto, url_archivo, url_clic, sub_tipo):
        super().__init__(ancho, alto, url_archivo, url_clic, sub_tipo)

    def comprimir_anuncio(self):
        print("COMPRESIÓN DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        print("REDIMENSIONAMIENTO DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADO AÚN")