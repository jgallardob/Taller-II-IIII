

class Parlamentario(object):
    """
    Clase que se encarga de abstraer la informacion de los parlamentarios
    scrappeados
    """
    def __init__(self, Id, nombre, AP, AM, sexo):
        """
        Constructor de la clase Parlamentario
        :param Id    : Id del parlamentario
        :param nombre: Nombre del parlamentario
        :param AP    : Apellido Paterno
        :param AM    : Apellido Materno
        :param sexo  : Sexo
        """
        self.Id = Id
        self.nombre = nombre
        self.AP = AP
        self.AM = AM
        self.sexo = sexo