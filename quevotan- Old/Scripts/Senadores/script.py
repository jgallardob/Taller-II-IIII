#-*- coding: utf-8 -*-
#Scraping votation data
#Juan Gallardo Beltran
#Computer Science School
#Catholic University of Temuco
#Professor: Julio Rojas


#LIBRARY IMPORTATION
import pymongo, sys, urllib2
from pymongo import MongoClient
import bs4 as BS 
from datetime import datetime
from dateutil.parser import parse
import pandas as pd


#FUNCTIONS
def carga_senadores():
	db.Senadores.insert({"A":"Allamand Z., Andrés", "B": "RN"});
	db.Senadores.insert({"A":"Allende B., Isabel", "B": "PS"});
	db.Senadores.insert({"A":"Araya G., Pedro", "B": "IND"});
	db.Senadores.insert({"A":"Bianchi C., Carlos", "B": "IND"});
	db.Senadores.insert({"A":"Chahuán C., Francisco", "B": "RN"});
	db.Senadores.insert({"A":"Coloma C., Juan Antonio", "B": "UDI"});
	db.Senadores.insert({"A":"De Urresti L., Alfonso", "B": "PS"});
	db.Senadores.insert({"A":"Espina O., Alberto", "B": "RN"});
	db.Senadores.insert({"A":"García Huidobro S., Alejandro", "B": "UDI"});
	db.Senadores.insert({"A":"García R., José", "B": "RN"});
	db.Senadores.insert({"A":"Girardi L., Guido", "B": "PPD"});
	db.Senadores.insert({"A":"Goic B., Carolina", "B": "PDC"});
	db.Senadores.insert({"A":"Guillier Á., Alejandro", "B": "IND"});
	db.Senadores.insert({"A":"Harboe B., Felipe", "B": "PPD"});
	db.Senadores.insert({"A":"Horvath K., Antonio", "B": "IND"});
	db.Senadores.insert({"A":"Lagos W., Ricardo", "B": "PPD"});
	db.Senadores.insert({"A":"Larraín F., Hernán", "B": "UDI"});
	db.Senadores.insert({"A":"Letelier M., Juan Pablo", "B": "PS"});
	db.Senadores.insert({"A":"Matta A., Manuel Antonio", "B": "PDC"});
	db.Senadores.insert({"A":"Montes C., Carlos", "B": "PS"});
	db.Senadores.insert({"A":"Moreira B., Iván", "B": "UDI"});
	db.Senadores.insert({"A":"Muñoz D., Adriana", "B": "PPD"});
	db.Senadores.insert({"A":"Navarro B., Alejandro", "B": "PAIS"});
	db.Senadores.insert({"A":"Orpis B., Jaime", "B": "UDI"});
	db.Senadores.insert({"A":"Ossandón I., Manuel José", "B": "RN"});
	db.Senadores.insert({"A":"Pérez S., Lily", "B": "AMP"});
	db.Senadores.insert({"A":"Pérez V., Víctor", "B": "UDI"});
	db.Senadores.insert({"A":"Pizarro S., Jorge", "B": "PDC"});
	db.Senadores.insert({"A":"Prokurica P., Baldo", "B": "RN"});
	db.Senadores.insert({"A":"Quintana L., Jaime", "B": "PPD"});
	db.Senadores.insert({"A":"Quinteros L., Rabindranath", "B": "PS"});
	db.Senadores.insert({"A":"Rossi C., Fulvio", "B": "PS"});
	db.Senadores.insert({"A":"Tuma Z., Eugenio", "B": "PPD"});
	db.Senadores.insert({"A":"Van Rysselberghe H., Jacqueline", "B": "UDI"});
	db.Senadores.insert({"A":"Von Baer J., Ena", "B": "UDI"});
	db.Senadores.insert({"A":"Walker P., Ignacio", "B": "PDC"});
	db.Senadores.insert({"A":"Walker P., Patricio", "B": "PDC"});
	db.Senadores.insert({"A":"Zaldívar L., Andrés", "B": "PDC"});

def get_data_votaciones(url, url_idpa):
	url_idpa = str(url_idpa)
	votacion = []
	source	 = urllib2.urlopen(url).read()
	soup 	 = BS.BeautifulSoup(source, 'lxml')
	orden	 = 0
	if soup.text=="\n":
		print "Archivo Vacio, registo ",url_idpa
	else:
		for res in soup.find_all('votacion'):
			date 		= res.find('fecha')
			fecha		= datetime.strptime(date.text, '%d/%m/%Y')
			fecha_ref	= datetime.strptime('11/03/2014', '%d/%m/%Y')
			if str(fecha_ref)>str(fecha):
				print "Votacion no corresponde a la legislatura iniciada el ",fecha_ref
			else:
				for res in soup.find_all('voto'):
					for c in res:
						orden = orden + 1
						Senador		= res.find('parlamentario').text
						Votacion 	= res.find('seleccion').text
						if Votacion=="Si":
							Votacion = 1
						if Votacion=="No":
							Votacion = 4
						if Votacion=="Abstencion" or Votacion=="Pareo":
							Votacion = 7
						if Votacion=="Dispensado":
							Votacion = 0
				#print orden
				id_vota = str(url_idpa)+str('-')+str(orden)
				#+str(datetime.now())
				db.Senadores.update({'A' : Senador}, {'$set' : {id_vota:Votacion}})
				db.Senadores.update_many({id_vota: None},{'$set':{id_vota: 0}});
				print "Insertada la votacion ",id_vota
	

#DATA PARAMETERS
url_base = "http://www.senado.cl/wspublico/votaciones.php?boletin="
url_idpa = 0

#Data Conecction with de MongoDB
client = MongoClient('localhost',27017)
#Get the Local Database
db = client['local']
#Delete Collection if exists
db.Senadores.drop()
#Create the collection
db.create_collection('Senadores',)
print "Data Collection created"
#Reload Sys and call default encoding
reload(sys)
sys.setdefaultencoding('utf-8')
carga_senadores()
while url_idpa<18000:
	cad = str(url_base)+str(url_idpa)
	get_data_votaciones(cad, url_idpa)
	url_idpa+=1
print "Finalizado . . . "