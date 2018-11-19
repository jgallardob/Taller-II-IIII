# coding=utf-8
from bs4 import BeautifulSoup as BS
import requests


class Votacion(object):
    def __init__(self, Id, Id_Diputado, voto):
        self.Id = Id
        self.Id_Diputado = Id_Diputado
        self.voto = voto
