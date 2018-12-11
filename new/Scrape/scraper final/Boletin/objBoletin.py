from bs4 import BeautifulSoup as BS
import requests


class Boletin(object):
    def __init__(self, _id):
        self._id = _id
