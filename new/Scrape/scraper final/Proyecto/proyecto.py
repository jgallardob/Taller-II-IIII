# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup as BS
import requests


class Proyecto(object):
    def __init__(self, _id, nombre, id_votacion, materia):
        self._id = _id
        self.nombre = nombre
        self.id_votacion = id_votacion
        self.materia = materia
