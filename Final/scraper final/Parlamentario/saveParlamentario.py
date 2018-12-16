# Extraccion de datos en forma de objetos para facilitar la insercion a MongoDB
import pymongo
from pymongo import MongoClient
from pprint import pprint
from parlamentarios import diputado as dt

client = MongoClient('localhost', 27017)
db = client.integracion
#----Obtencion de datos diputado como objeto---->
for diputados in dt.Diputado.getParlamentarios():
    # print diputados.Id + " " + diputados.nombre + " " + diputados.apellido_paterno \
    #    + " " + diputados.region + " " + diputados.distrito + " " + diputados.partido
    db.Parlamentario.insert(diputados.__dict__) #guardamos la coleccion parlamentario


client.close()
