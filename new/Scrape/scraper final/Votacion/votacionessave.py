# -*- coding: utf-8 -*-
# Extraccion de datos en forma de objetos para facilitar la insercion a MongoDB
import pymongo
from pymongo import MongoClient
from pprint import pprint
from votaciones import Votacion


client = MongoClient('localhost', 27017)
db = client.integracion
#----Obtencion de datos diputado como objeto---->
for i in Votacion.get_Votaciones():
    #print i.__dict__
    db.votacion.insert(i.__dict__)
print "Proyectos descargadas y guardadas en MongoDB(:"

client.close()
