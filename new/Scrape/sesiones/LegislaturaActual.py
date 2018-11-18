from bs4 import BeautifulSoup as BS
import requests


class Legislatura(object):
    pass


Leg = Legislatura()


def GetLegislaturaActual():
    Url_LegislaturaActual = "http://opendata.camara.cl/camaradiputados/WServices/WSLegislativo.asmx/retornarLegislaturaActual?"
    r = requests.get(Url_LegislaturaActual)
    data = r.text
    soup = BS(data, 'xml')
    result = soup.find("Legislatura")
    Leg.Id = result.Id.text.encode('utf-8')
    Leg.numero = result.Numero.text.encode('utf-8')
    Leg.fecha_inicio = result.FechaInicio.text.encode('utf-8')
    Leg.fecha_termino = result.FechaTermino.text.encode('utf-8')
    # print Id + numero + fecha_inicio + fecha_termino
    return Leg
