# -*- coding: utf-8 -*-
import os
import sys
sys.path.insert(0, os.path.realpath('../'))
from bs4 import BeautifulSoup as BS
import requests
from listado import Listado

class Proyectos(Listado):
    votaciones = {}
    @classmethod
    def getProyectos(cls, _id):
        proyectos = []
        Url_Proyecto = "http://opendata.camara.cl/camaradiputados/WServices/WSLegislativo.asmx/retornarProyectoLey?prmNumeroBoletin=" + str(_id)
        r = requests.get(Url_Proyecto)
        data = r.text
        soup = BS(data, 'xml')
        proyecto = soup.find("ProyectoLey")
        votacion = soup.find_all("VotacionProyectoLey")
        materia = soup.find("Materia")
        if (soup.find("VotacionProyectoLey")):
            _id = proyecto.Id.text.encode("utf-8")
            nombre = proyecto.Nombre.text.encode("utf-8")
            for j in votacion:
                id_votacion = j.Id.text.encode("utf-8")
            try:
                materia = materia.Nombre.text.encode("utf-8")
            except AttributeError:
                materia = None

            proyectos.append(cls.toObject(_id, nombre, id_votacion, materia))
        return proyectos
