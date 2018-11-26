

class Voto(object):
    """
    Clase que se encarga de abstraer la informacion obtenido de los votos dentro
    de x periodo legislativo
    """
    def __init__(self, Id, parlamentario, valor):
        """
        Constructor de la clase Parlamentario
        :param Id           : Id del voto
        :param parlamentario: Nombre del parlamentario
        :param valor        : Que significa el voto
        """
        self.Id = Id
        self.parlamentario = parlamentario
        self.valor = valor