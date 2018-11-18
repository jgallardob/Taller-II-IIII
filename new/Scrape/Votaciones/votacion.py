# coding=utf-8
from bs4 import BeautifulSoup as BS
import requests


class Votacion(object):
    def __init__(self, Id_Diputado, voto):
        self.Id_Diputado = Id_Diputado
        self.voto = voto
