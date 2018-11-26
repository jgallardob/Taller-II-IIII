
from bs4 import BeautifulSoup as BS
import requests
from sesion import Sesion

class Legislatura(Sesion):
    @classmethod
    def getSesiones(cls):
        sesiones = []
        Url_Sesion = "http://opendata.camara.cl/camaradiputados/WServices/WSSala.asmx/retornarSesionesXLegislatura?prmLegislaturaId=50"# + str(GetLegislaturaActual().Id)
        r = requests.get(Url_Sesion)
        data = r.text
        soup = BS(data, 'xml')
        result = soup.find_all("Sesion")
        for sesion in result:
            _id = sesion.Id.text.encode('utf-8')
            numero = sesion.Numero.text.encode('utf-8')
            FechaInicio = sesion.FechaInicio.text.encode('utf-8')
            FechaTermino = sesion.FechaTermino.text.encode('utf-8')
            sesiones.append(Sesion(_id, numero, FechaInicio, FechaTermino))
        return sesiones