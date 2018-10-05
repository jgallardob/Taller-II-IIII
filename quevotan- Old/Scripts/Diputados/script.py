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

#DATA PARAMETERS
url_base = "http://opendata.congreso.cl/wscamaradiputados.asmx/getVotacion_Detalle?prmVotacionID="
url_idpa = 19192

#FUNCTIONS

#GET PARTY AND NAME OF PARLAMENTARY
def get_nombre_partido():
	url    		= "http://opendata.camara.cl/wscamaradiputados.asmx/getDiputados_Vigentes"
	source 		= urllib2.urlopen(url).read()
	soup   		= BS.BeautifulSoup(source, 'lxml')
	diputado 	= []
	for lis in soup.find_all('diputado'):
		codigo		= lis.find('dipid').text
		name		= lis.find('nombre').text
		ape1		= lis.find('apellido_paterno').text
		ape2		= lis.find('apellido_materno').text
		for par in lis.find_all('militancia_actual'):
			part = par.find('partido').text
			if part=="Independientes":
				part = "IND"
			if part=="Unión Demócrata Independiente":
				part = "UDI"
			if part=="Partido Por la Democracia":
				part = "PPD"
			if part=="Partido Demócrata Cristiano":
				part = "PDC"
			if part=="Partido Liberal de Chile":
				part = "PL"
			if part=="Partido Comunista":
				part = "PC"
			if part=="Partido Socialista":
				part = "PS"
			if part=="Partido Radical Social Demócrata":
				part = "PRSD"
			if part=="Renovación Nacional":
				part = "RN"
			if part=="Revolución Democrática":
				part = "RD"
			if part=="Evópoli":
				part = "EV"
			if part=="Amplitud":
				part = "AMP"
			if part=="Izquierda Ciudadana":
				part = "IC"
			cad 	= str(ape1)+str(" ")+str(ape2)+str(" ")+str(name)
			db.Diputados.save({'A' : cad, 'B' : part});
		diputado = []


#GET VOTATION SESION
def get_votacion_sesion(url, url_idpa):
	url_idpa = str(url_idpa)
	votacion = []
	source	 = urllib2.urlopen(url).read()
	soup 	 = BS.BeautifulSoup(source, 'lxml')
	if soup.text=="":
		print "Archivo Vacio, registo ",url_idpa
	else:
		for res in soup.find_all('voto'):
			for c in res:
				Nombre 		= res.find('nombre').text
				Apellido1	= res.find('apellido_paterno').text
				Apellido2 	= res.find('apellido_materno').text
				Votacion 	= res.find('opcion').text
				if Votacion=="AFIRMATIVO":
					Votacion = 1
				if Votacion=="EN CONTRA":
					Votacion = 4
				if Votacion=="ABSTENCION" or Votacion=="PAREO":
					Votacion = 7
				if Votacion=="DISPENSADO":
					Votacion = 0
				cad = str(Apellido1)+str(" ")+str(Apellido2)+str(" ")+str(Nombre)
			id_vota = str('vot')+ str(url_idpa)
			#ADDING DATA TO MONGO DATABASE
			db.Diputados.update({'A' : cad}, {'$set' : {id_vota:Votacion}})
			db.Diputados.update_many({id_vota: None},{'$set':{id_vota: 0}});
			votacion = []
		print "Insertando el registro ", url_idpa

#RUN PROGRAM

#DATA CONECTION WITH MONGODB
client 		= MongoClient('localhost', 27017 )
db 			= client['local']
db.Diputados.drop()
db.create_collection('Diputados',)
reload(sys)
sys.setdefaultencoding('utf-8')
get_nombre_partido()
while url_idpa<30000:
	obj = str(url_base)+str(url_idpa)
	get_votacion_sesion(obj, url_idpa)
	url_idpa+=1
print "Finalizado . . ."