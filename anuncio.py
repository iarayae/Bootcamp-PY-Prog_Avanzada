# Clase base Anuncio
# Servirá como clase padre para los tipos específicos de anuncios
class Anuncio:
    pass  # se definirá más adelante como clase abstracta

# Clase Video que hereda de Anuncio
# Define atributos de clase especificos para el tipo de anuncio "Video"
class Video(anuncio):
    FORMATO = "Video" # Tipo de formato
    SUB_TIPOS = ("instream", "outstream") # subtipos válidos para anuncios en video

# Clase Display que hereda tambien de Anuncio
# Define atributos de clase especificos para el tipo de anuncio "Display"
class Display(Anuncio):
    FORMATO = "Display" # Tipo de Formato
    SUB_TIPOS = ("tradicional", "native") # subtipos validos para este tipo de anuncio

# Clase Social que hereda de Anuncio
# Define atributos de clase especificos para el tipo de anuncio en redes sociales
class Social(Anuncio):
    FORMATO = "Social"
    SUB_TIPOS = ("facebook", "linkedin")