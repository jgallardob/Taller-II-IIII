# Extraccion de datos en forma de objetos para facilitar la insercion a MongoDB
import pymongo
from pymongo import MongoClient
from pprint import pprint
from votaciones import Votaciones

client = MongoClient('localhost', 27017)
db = client.integracion
#----Obtencion de datos diputado como objeto---->
for i in Votaciones.get_Votaciones():
    print i.__dict__  # cambiar a base de datos claudio 
    				  #	(para modificar cantidad de votaciones ir a votaciones.py
    				  #  y cambiar el rango en la linea 23 OJO!) 	

client.close()