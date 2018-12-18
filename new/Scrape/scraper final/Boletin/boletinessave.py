# -*- coding: utf-8 -*-
# Extraccion de datos en forma de objetos para facilitar la insercion a MongoDB
from pymongo import MongoClient
from boletines import Boletines

client = MongoClient('localhost', 27017)
db = client.integracion
#----Obtencion de datos diputado como objeto---->

for i in Boletines.getBoletines():
    print i.__dict__
    db.boletin.insert(i.__dict__)
print "Boletines descargadas y guardadas en MongoDB (:"
client.close()
