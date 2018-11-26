# Extraccion de datos en forma de objetos para facilitar la insercion a MongoDB
import pymongo
from pymongo import MongoClient
from pprint import pprint
from sesiones import Sesiones

client = MongoClient('localhost', 27017)
db = client.integracion
#----Obtencion de datos diputado como objeto---->
for i in Sesiones.get_Sesiones():
    print i.__dict__
    db.sesion.insert(i.__dict__)
print "Sesiones descargadas y guardadas en MongoDB (:"

client.close()
