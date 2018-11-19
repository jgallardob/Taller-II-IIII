from bs4 import BeautifulSoup as BS
import requests


class Sesion(object):
    def __init__(self, _id, numero, fecha_inicio, fecha_termino):
        self._id = _id
        self.numero = numero
        self.fecha_inicio = fecha_inicio
        self.fecha_termino = fecha_termino
