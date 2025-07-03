# Clase base para las excepciones personalizadas del sistema
class Error(Exception):
    def __init__(self, mensaje):
        super().__init__(mensaje)
        self.mensaje = mensaje

    def __str__(self):
        return f"[ERROR] {self.mensaje}"


# Excepción lanzada cuando el nombre de la campaña excede los 250 caracteres
class LargoExcedidoError(Error):
    def __init__(self, mensaje="El nombre supera el largo permitido."):
        super().__init__(mensaje)


# Excepción lanzada cuando se asigna un subtipo no válido
class SubTipoInvalidoError(Error):
    def __init__(self, mensaje="El subtipo ingresado no es válido para este tipo de anuncio."):
        super().__init__(mensaje)