# Bootcamp-PY-Prog_Avanzada
Bootcamp - PY - Programación Avanzada Examen

## Objetivo General ## 

Modelar un sistema de campañas publicitarias que incluye anuncios de distintos tipos (Video, Display, Social), aplicando herencia, encapsulamiento, abstracción, polimorfismo, composición, colaboración entre clases y manejo de excepciones.

## Archivos incluidos ##

- 'campaña.py': Contiene la clase 'Campaña', que representa una campaña publicitaria con múltiples anuncios.
- 'anuncio.py': Contiene la clase abstracta 'Anuncio' y sus subclases 'Video', 'Display' y 'Social', cada una con atributos y comportamientos específicos.
- 'error.py': Define excepciones personalizadas ('Error', 'LargoExcedidoError', 'SubTipoInvalidoError') utilizadas en el sistema.
- 'demo.py': Script interactivo que permite probar la modificación de atributos en una campaña y registra errores en un archivo 'error.log'.
- 'error.log': Archivo donde se almacenan los mensajes de error generados por las excepciones lanzadas.

## Requisitos cumplidos ##

1. Creación de clases y atributos estáticos
   - Clases definidas con atributos de clase 'FORMATO' y 'SUB_TIPOS'.

2. Sobrecarga de funciones especiales
   - '__init__' personalizado en todas las clases.
   - '__str__' en 'Campaña' muestra nombre y cantidad de anuncios por tipo.

3. Programación orientada a objetos
   - Herencia entre 'Anuncio' y sus subclases.
   - Métodos abstractos implementados.
   - Encapsulamiento y validaciones en los atributos con 'getter' y 'setter'.

4. Colaboración y composición
   - 'Campaña' crea internamente sus anuncios a partir de datos recibidos.
   - Método estático 'mostrar_formatos' en 'Anuncio' muestra los subtipos disponibles.

5. Manejo de excepciones y escritura de archivos
   - Excepciones personalizadas lanzadas donde corresponde.
   - 'demo.py' registra errores en 'error.log'.
