
from bs4 import BeautifulSoup as BS
import requests
from listado import Listado
from LegislaturaActual import GetLegislaturaActual


class Sesiones(Listado):
    @classmethod
    def get_Sesiones(cls):
        sesiones = []
        Url_Sesion = "http://opendata.camara.cl/camaradiputados/WServices/WSSala.asmx/retornarSesionesXLegislatura?prmLegislaturaId=" + str(GetLegislaturaActual().Id)
        r = requests.get(Url_Sesion)
        data = r.text
        soup = BS(data, 'xml')
        result = soup.find_all("Sesion")
        for i in result:
            Id = i.Id.text.encode('utf-8')
            numero = i.Numero.text.encode('utf-8')
            FechaInicio = i.FechaInicio.text.encode('utf-8')
            FechaTermino = i.FechaTermino.text.encode('utf-8')
            sesiones.append(cls.toObject(Id, numero, FechaInicio, FechaTermino))
        return sesiones
