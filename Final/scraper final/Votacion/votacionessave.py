# -*- coding: utf-8 -*-
# Extraccion de datos en forma de objetos para facilitar la insercion a MongoDB
from pymongo import MongoClient
from votaciones import Votaciones


client = MongoClient('localhost', 27017)
db = client.integracion
#----Obtencion de datos diputado como objeto---->
for voto in Votaciones.getVotaciones():
    print voto.Id
    db.votacion.insert(voto.__dict__)
print "Proyectos descargadas y guardadas en MongoDB(:"

client.close()
