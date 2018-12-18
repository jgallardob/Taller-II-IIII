# -*- coding: utf-8 -*-
import os
import sys
sys.path.insert(0, os.path.realpath('../'))

from bs4 import BeautifulSoup as BS
import requests
from listado import Listado
from sesiones.sesiones import Sesiones
import re


class Boletines(Listado):
    proyectos = {}
    @classmethod
    def getBoletines(cls, _id):
        boletines = []
        array = []
        regex = re.compile(r"[0-9]")

        Url_Boletin = "http://opendata.camara.cl/wscamaradiputados.asmx/getSesionBoletinXML?prmSesionID=" + str(_id)
        r = requests.get(Url_Boletin)
        data = r.text
        soup = BS(data, 'xml')
        boli = soup.find_all("PROYECTO_LEY")

        for i in boli:
            bole = i["BOLETIN"]
            bole = re.split('[ , .]', bole)
            for bo in bole:
                if regex.search(bo):
                    array.append(bo)
        aset = set(array)
        for j in aset:
            j = j.encode('utf-8')
            boletines.append(cls.toObject(str(j)))
        return boletines
