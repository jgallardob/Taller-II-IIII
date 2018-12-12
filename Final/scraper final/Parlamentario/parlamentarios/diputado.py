import os
import sys
sys.path.insert(0, os.path.realpath('../'))

from listado import Listado
from bs4 import BeautifulSoup as BS
import requests


import base64
from PIL import Image, ImageOps


class Diputado(Listado):
    @classmethod
    def getParlamentarios(cls):
        url_ids = "http://opendata.camara.cl/camaradiputados/WServices/WSDiputado.asmx/retornarDiputadosPeriodoActual?"
        r_id = requests.get(url_ids)
        data_id = r_id.text
        soup_id = BS(data_id, 'xml')
        ids = soup_id.find_all("Diputado")

        DiputadosId = []
        nombres = []
        apellidos = []
        imagenes = []

        for i in ids:
            DiputadosId.append(i.Id.text)

        for i in DiputadosId:
            url_detalle = "http://opendata.camara.cl/camaradiputados/WServices/WSDiputado.asmx/retornarDiputado?prmDiputadoId=" + str(i)
            r = requests.get(url_detalle)
            data = r.text
            soup = BS(data, 'xml')
            result1 = soup.find("Diputado")
            nombres.append(result1.Nombre.text.replace(" ", "-"))
            apellidos.append(result1.ApellidoPaterno.text.replace(" ", "-"))

        Url_detalle_2 = "http://www.camara.cl/camara/diputados.aspx#tab"
        r = requests.get(Url_detalle_2)
        data = r.text
        soup = BS(data, 'xml')
        diputados = soup.find_all('li', {'class': 'alturaDiputado'})
        info = soup.find_all('li', {'class': 'alturaDiputado'})
        foto = soup.find_all('div', {'class': 'imgSet'})

        c = 1
        for i in range(5, len(foto) - 1):
            src = foto[i].img['src']
            imagen_base = 'http://www.camara.cl' + src
            response = requests.get(imagen_base)
            if response.status_code == 200:
                with open("fotos/diputado " + str(c) + ".jpg", 'wb') as f:
                    f.write(response.content)
                    print "imagen " + str(c) + " guardada"
                    c += 1

        for i in range(1, 156):
            with open("fotos/diputado " + str(i) + ".jpg", "rb") as image_file:
                imagenes.append(base64.b64encode(image_file.read()))
                i += 1

        parl = []

        for i in range(0, len(info)):
            _id = DiputadosId[i]
            nombre = nombres[i]
            apellido_paterno = apellidos[i]
            print imagenes[i]
            imagen = imagenes[i]
            region = info[i].find("ul").text.split()[1]
            distrito = info[i].find("ul").text.split()[3]
            partido = info[i].find("ul").text.split()[5]

            parl.append(cls.toObject(_id, nombre, apellido_paterno, imagen, region, distrito, partido))
        return parl
