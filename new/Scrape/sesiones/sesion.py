from bs4 import BeautifulSoup as BS
import requests


class Sesion(object):
    def __init__(self, Id, numero, fecha_inicio, fecha_termino):
        self.Id = Id
        self.numero = numero
        self.fecha_inicio = fecha_inicio
        self.fecha_termino = fecha_termino
