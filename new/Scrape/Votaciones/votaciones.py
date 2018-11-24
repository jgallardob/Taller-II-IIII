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
        aId_votaciones = []

        for i in ids_votacion[0:3]:  # (manejar cantidad de votaciones, linea 38 debe tener mislo largo)
            Url_VotaDetalle = "http://opendata.camara.cl/camaradiputados/WServices/WSLegislativo.asmx/retornarVotacionDetalle?prmVotacionId=" + str(i)
            r = requests.get(Url_VotaDetalle)
            data = r.text
            soup = BS(data, 'xml')

            result2 = soup.find_all("Voto")
            for i in result2:
                aId_Diputados.append(i.Id.text)
                # aVotos.append(i.OpcionVoto["Valor"])
                if i.OpcionVoto["Valor"] == "0":
                    aVotos.append("4")
                if i.OpcionVoto["Valor"] == "1":
                    aVotos.append("1")
                if i.OpcionVoto["Valor"] == "2":
                    aVotos.append("7")

        votaciones = []

        for i in range(0, len(ids_votacion[0:3])):  # (manejar cantidad de votaciones, linea 24 debe tener mislo largo)
            for j in range(0, len(aId_Diputados)):
                Id = ids_votacion[i]
                Id_Diputado = str(aId_Diputados[j])
                voto = aVotos[j]

                votaciones.append(cls.toObject(Id, Id_Diputado, voto))

        return votaciones
