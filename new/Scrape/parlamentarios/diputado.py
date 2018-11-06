import os
import sys
sys.path.insert(0, os.path.realpath('../'))

from listado import Listado

from bs4 import BeautifulSoup as BS
import requests

class Diputado(Listado):
    @classmethod
    def getParlamentarios(cls):
        base = 'http://opendata.camara.cl/camaradiputados/WServices/WSDiputado.asmx/retornarDiputados?'
        r = requests.get(base)
        data = r.text
        soup = BS(data, 'xml')

        diputados = soup.find_all("Diputado")

        if not diputados:
            return ['Lista vacia']

        parl = []
        for diputado in diputados:
            Id = diputado.Id.text.encode('utf-8')
            nombre = diputado.Nombre.text.encode('utf-8')
            AP = diputado.ApellidoPaterno.text.encode('utf-8')
            AM = diputado.ApellidoMaterno.text.encode('utf-8')
            sexo = diputado.Sexo.text.encode('utf-8')
            try:
                partido = diputado.Militancias.Militancia.Partido.Alias.text.encode('utf-8')
            except:
                partido = 'Null'
                pass
            parl.append(cls.toObject(Id, nombre, AP, AM, sexo, partido))
        return parl
