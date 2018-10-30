#Extraccion de datos en forma de objetos para facilitar la insercion a MongoDB
import pymongo
from pymongo import MongoClient
from pprint import pprint
from parlamentarios import Diputado

client=MongoClient('localhost',27017)
db=client.integracion
#----Obtencion de datos diputado como objeto---->
for diputados in Diputado.getParlamentarios():
    #print diputados #Cambiar por subir a DB
    db.parlamentario.insert(diputados.__dict__)

client.close()