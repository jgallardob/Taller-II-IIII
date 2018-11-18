# coding=utf-8

from bs4 import BeautifulSoup as BS
import requests
from listado import Listado


class Votaciones(Listado):
    @classmethod
    def get_Votaciones(cls):
        ids_votacion = []
        Url_VotaXanio = "http://opendata.camara.cl/camaradiputados/WServices/WSLegislativo.asmx/retornarVotacionesXAnno?prmAnno=" + str(2018)
        r = requests.get(Url_VotaXanio)
        data = r.text
        soup = BS(data, 'xml')
        result = soup.find_all("Votacion")
        for i in result:
            ids_votacion.append(i.Id.text.encode('utf-8'))

        aId_Diputados = []
        aVotos = []

        for i in ids_votacion[0:3]:  # (manejar cantidad de votaciones)
            Url_VotaDetalle = "http://opendata.camara.cl/camaradiputados/WServices/WSLegislativo.asmx/retornarVotacionDetalle?prmVotacionId=" + str(i)
            r = requests.get(Url_VotaDetalle)
            data = r.text
            soup = BS(data, 'xml')
            result = soup.find_all("Voto")
            for i in result:
                aId_Diputados.append(i.Id.text.encode('utf-8'))
                aVotos.append(i.OpcionVoto["Valor"].encode('utf-8'))

        votaciones = []

        for i in range(0, len(aId_Diputados)):
            Id_Diputado = aId_Diputados[i]
            voto = aVotos[i]

            votaciones.append(cls.toObject(Id_Diputado, voto))
        return votaciones
