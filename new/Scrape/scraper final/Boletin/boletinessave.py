# -*- coding: utf-8 -*-
# Extraccion de datos en forma de objetos para facilitar la insercion a MongoDB
import pymongo
from pymongo import MongoClient
from pprint import pprint
from boletines import Boletin

client = MongoClient('localhost', 27017)
db = client.integracion
#----Obtencion de datos diputado como objeto---->

for i in Boletin.get_Boletines():
    print i.__dict__
    db.boletin.insert(i.__dict__)
print "Boletines descargadas y guardadas en MongoDB (:"
client.close()
