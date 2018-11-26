import os
import sys
sys.path.insert(0, os.path.realpath('../'))
from bs4 import BeautifulSoup as BS
import requests
from listado import Listado
from legislatura.legislaturas import Legislatura


class Sesiones(Listado):
    @classmethod
    def get_Sesiones(cls):
        print "Descargando Sesiones...espere"
        legislaturas = []

        legislaturas.append(Legislatura.get_Legislaturas()[-1]._id)  # Ultima legislatura(50)(con un for obetenemos todas)

        for i in legislaturas:
            sesiones = []
            Url_Sesion = "http://opendata.camara.cl/wscamaradiputados.asmx/getSesiones?prmLegislaturaID=" + str(i)
            r = requests.get(Url_Sesion)
            data = r.text
            soup = BS(data, 'xml')
            sesi = soup.find_all("Sesion")
            for i in sesi:
                _id = i.ID.text.encode('utf-8')
                Fecha = i.Fecha.text.encode('utf-8')
                tipo = i.Tipo.text.encode('utf-8')
                estado = i.Estado.text.encode('utf-8')
                sesiones.append(cls.toObject(_id, Fecha, tipo, estado))
        return sesiones
