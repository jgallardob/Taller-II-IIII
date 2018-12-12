# -*- coding: utf-8 -*-
import os
import sys
sys.path.insert(0, os.path.realpath('../'))
from bs4 import BeautifulSoup as BS
import requests
from listado import Listado
from Proyecto.proyectos import Proyectos


class Votaciones(Listado):
    @classmethod
    def getVotaciones(cls):
        votaciones = []
        for p in Proyecto.get_Proyectos():
            votaciones.append(p.id_votacion)

        aId_Diputados = []
        aVotos = []
        vot = []

        for ids in votaciones[0:2]:  # (manejar cantidad de votaciones)
            Url_VotaDetalle = "http://opendata.camara.cl/camaradiputados/WServices/WSLegislativo.asmx/retornarVotacionDetalle?prmVotacionId=" + str(ids)
            r = requests.get(Url_VotaDetalle)
            data = r.text
            soup = BS(data, 'xml')
            voto = soup.find_all("Voto")
            for i in voto:
                aId_Diputados.append(i.Id.text)
                if i.OpcionVoto["Valor"] == "0":
                    aVotos.append("4")
                if i.OpcionVoto["Valor"] == "1":
                    aVotos.append("1")
                if i.OpcionVoto["Valor"] == "2":
                    aVotos.append("7")

            Id = str(ids)
            for i in range(0, len(aVotos)):
                Id_Diputado = str(aId_Diputados[i])
                voto = str(aVotos[i])

                vot.append(cls.toObject(Id, Id_Diputado, voto))
        return vot
