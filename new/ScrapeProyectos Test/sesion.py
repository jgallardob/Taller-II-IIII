
from bs4 import BeautifulSoup as BS
import requests

class Sesion(object):
    """
    Clase que se encarga de abstraer la informacion obtenido de los votos dentro
    de x periodo legislativo
    """
    def __init__(self, _id, numero, FechaInicio, FechaTermino):
        """
        Constructor de la clase Parlamentario
        :param Id           : Id del voto
        :param parlamentario: Nombre del parlamentario
        :param valor        : Que significa el voto
        """
        self._id = _id
        self.numero = numero
        self.FechaInicio = FechaInicio
        self.FechaTermino = FechaTermino
        self.proyectos = self.getBoletines()

    def getBoletines(cls):
        url = 'http://opendata.camara.cl/wscamaradiputados.asmx/getSesionBoletinXML?prmSesionID=' + str(cls._id)
        r = requests.get(url)
        data = r.text
        soup = BS(data, 'xml')
        result = soup.find_all("PROYECTO_LEY")
        boletines = []
        for boletin in result:
            #PROCESAR ANTES BOLETIN
            data = boletin['BOLETIN']
            data = data.split()
            boletines.append(data)
            print data
        print 'passSESION'
        print cls._id
        return boletines


