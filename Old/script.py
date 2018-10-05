#Extraccion de ID y datos
#Juan Gallardo Beltran
#Temuco, Octubre de 2017

#-*- coding: utf-8 -*-
#Libraries Import
import bs4 as BS 
import urllib2
import sys

legislaturas = []
boletines = []
all_votaciones = []

def get_sesion(id):
	id = str(id)
	url = "http://opendata.camara.cl/wscamaradiputados.asmx/getSesiones?prmLegislaturaID="+id
	source = urllib2.urlopen(url).read()
	soup   = BS.BeautifulSoup(source, 'lxml')
	for pagina in soup.find_all('id'):
		dato = pagina.text
		legislaturas.append(dato)
	for t in legislaturas:
		get_boletin_sesion(t)

def get_boletin_sesion(id):
	id = str(id)
	url = "http://opendata.camara.cl/wscamaradiputados.asmx/getSesionBoletinXML?prmSesionID="+id
	source = urllib2.urlopen(url).read()
	soup   = BS.BeautifulSoup(source, 'lxml')
	for pagina in soup.find_all('tabla'):
		for c in pagina:
			boletin = pagina.find('Boletin N\\°')
			print boletin
		#dato = pagina
		#print dato

def id_votacion(id):
	id = str(id)
	url = "http://opendata.camara.cl/wscamaradiputados.asmx/getVotacion_Detalle?prmVotacionID="+id
	source = urllib2.urlopen(url).read()
	soup   = BS.BeautifulSoup(source, 'lxml')
	for res in soup.find_all('voto'):
		for c in res:
			Nombre = res.find('nombre').text
			Apellido1 = res.find("apellido_paterno").text
			Apellido2 = res.find("apellido_materno").text
			Votacion = res.find("opcion").text
			if Votacion=="AFIRMATIVO":
				Votacion = 1
			if Votacion=="EN CONTRA":
				Votacion = 4
			if Votacion=="ABSTENCION":
				Votacion = 7
			cad = str('"')+str(Apellido1)+" "+str(Apellido2)+" "+str(Nombre)+str('"')
		print cad, Votacion


reload(sys)
sys.setdefaultencoding('utf-8')
#get_sesion(48)
get_boletin_sesion(3327)