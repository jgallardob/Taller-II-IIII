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
    @classmethod
    def getBoletines(cls):
        sesiones = []
        boletines = []
        array = []
        regex = re.compile(r"[0-9]")

        for s in Sesiones.get_Sesiones():
            sesiones.append(s._id)

        for i in sesiones:
            Url_Boletin = "http://opendata.camara.cl/wscamaradiputados.asmx/getSesionBoletinXML?prmSesionID=" + str(i)
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
            boletines.append(cls.toObject(str(j)))
        return boletines
