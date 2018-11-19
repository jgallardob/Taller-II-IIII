

class Parlamentario(object):
    """
    Clase que se encarga de abstraer la informacion de los parlamentarios
    scrappeados
    """

    def __init__(self, _id, nombre, apellido_paterno, imagen, region, distrito, partido):
        """
        Constructor de la clase Parlamentario
        :param nombre: Nombre del parlamentario
        :param AP    : Apellido Paterno
        :param sexo  : Sexo
        """

        self._id = _id
        self.nombre = nombre
        self.apellido_paterno = apellido_paterno
        self.imagen = imagen
        self.region = region
        self.distrito = distrito
        self.partido = partido
