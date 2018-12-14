import os
import sys
sys.path.insert(0, os.path.realpath('../'))
from bs4 import BeautifulSoup as BS
import requests
from listado import Listado

class Sesiones(Listado):
    @classmethod
    def getSesiones(cls, _id):
        sesiones = []
        Url_Sesion = "http://opendata.camara.cl/wscamaradiputados.asmx/getSesiones?prmLegislaturaID=" + str(_id)
        r = requests.get(Url_Sesion)
        data = r.text
        soup = BS(data, 'xml')
        sesi = soup.find_all("Sesion")
        for i in sesi:
            _id = i.ID.text.encode('utf-8')
            Fecha = i.Fecha.text.encode('utf-8')
            Fecha = Fecha.split("T")[0]
            tipo = i.Tipo.text.encode('utf-8')
            estado = i.Estado.text.encode('utf-8')
            sesiones.append(cls.toObject(_id, Fecha, tipo, estado))
        return sesiones
