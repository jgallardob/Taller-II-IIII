# coding=utf-8
from bs4 import BeautifulSoup as BS
import requests


class Votacion(object):
    def __init__(self, _id, Id_Diputado, voto):
        self._id = _id
        self.Id_Diputado = Id_Diputado
        self.voto = voto
