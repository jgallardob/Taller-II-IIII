from bs4 import BeautifulSoup as BS
import requests


class Sesion(object):
    def __init__(self, _id, fecha, tipo, estado):
        self._id = _id
        self.fecha = fecha
        self.tipo = tipo
        self.estado = estado
