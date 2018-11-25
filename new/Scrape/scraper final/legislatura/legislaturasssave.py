# Extraccion de datos en forma de objetos para facilitar la insercion a MongoDB
import pymongo
from pymongo import MongoClient
from pprint import pprint
from legislaturas import Legislatura

client = MongoClient('localhost', 27017)
db = client.integracion
#----Obtencion de datos diputado como objeto---->

for i in Legislatura.get_Legislaturas():
    print i.__dict__
    db.legislatura.insert(i.__dict__)
print "Legislaturas descargadas y guardadas en MongoDB (:"
client.close()
