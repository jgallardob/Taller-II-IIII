
from bs4 import BeautifulSoup as BS
import requests
from listado import Listado


class Legislaturas(Listado):
    sesiones = {}

    @classmethod
    def getLegislaturas(cls):
        legislaturas = []
        #Url_legislaturas = "http://opendata.camara.cl/wscamaradiputados.asmx/getLegislaturas" # para todas la legis
        Url_legislaturas = "http://opendata.camara.cl/wscamaradiputados.asmx/getLegislaturaActual" # ultima legis
        r = requests.get(Url_legislaturas)
        data = r.text
        soup = BS(data, 'xml')
        legis = soup.find_all("Legislatura")
        for i in legis:
            _id = i.ID.text.encode('utf-8')
            numero = i.Numero.text.encode('utf-8')
            FechaInicio = i.FechaInicio.text.encode('utf-8')
            FechaInicio = FechaInicio.split("T")[0]
            FechaTermino = i.FechaTermino.text.encode('utf-8')
            FechaTermino = FechaTermino.split("T")[0]
            legislaturas.append(cls.toObject(_id, numero, FechaInicio, FechaTermino))
        return legislaturas
