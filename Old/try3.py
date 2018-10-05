#-*- coding: utf-8 -*-
#Script 3 Datos diputados
#Ejemplo con un Diputado
#Codigo Diputado 915

import bs4 as BS 
import urllib2
import sys
import csv

cod_diputados = [915]
diputado = []
legislaturas = []
boletines = []
all_votaciones = []


def get_datos(id_diputado):
	id_diputado = int(id_diputado)
	url = "http://opendata.camara.cl/wscamaradiputados.asmx/getDiputados_Vigentes"
	source = urllib2.urlopen(url).read()
	soup   = BS.BeautifulSoup(source, 'lxml')
	for lis in soup.find_all('diputado'):
		codigo = lis.find('dipid').text
		codigo = int(codigo)
		if id_diputado==codigo:
			name = lis.find('nombre').text
			ape1 = lis.find('apellido_paterno').text
			ape2 = lis.find('apellido_materno').text
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
				cad = str(name)+str(" ")+str(ape1)+str(" ")+str(ape2)
				diputado.append(cad)
				diputado.append(part)
				print diputado
				
def get_legislaturas(id):
	id = str(id)
	url = "http://opendata.camara.cl/wscamaradiputados.asmx/getSesiones?prmLegislaturaID="+id
	source = urllib2.urlopen(url).read()
	soup   = BS.BeautifulSoup(source, 'lxml')
	for pagina in soup.find_all('id'):
		dato = pagina.text
		legislaturas.append(dato)
	for t in legislaturas:
		get_boletin(t)

def get_boletin(id):
	id = str(id)
	url = "http://opendata.camara.cl/wscamaradiputados.asmx/getVotaciones_Boletin?prmBoletin="+id
	source = urllib2.urlopen(url).read()
	soup   = BS.BeautifulSoup(source, 'lxml')
	for pagina in soup.find_all('id'):
		parse = pagina.text
		parse = int(parse)
		boletines.append(parse)
	return boletines

def id_votacion(id, id_diputado):
	id_diputado = int(id_diputado)
	vot = str(id)
	url = "http://opendata.camara.cl/wscamaradiputados.asmx/getVotacion_Detalle?prmVotacionID="+vot
	source = urllib2.urlopen(url).read()
	soup   = BS.BeautifulSoup(source, 'lxml')
	for res in soup.find_all('voto'):
		codigo = res.find('dipid').text
		codigo = int(codigo)
		if id_diputado==codigo:
			print vot
			print codigo
			print "si voto"
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
			#print "Votacion : "+id
			#matriz(cad, Votacion)
			diputado.append(Votacion)
			print diputado


def matriz(nombre, votacion):
	pass

def exportar():
	pass


reload(sys)
sys.setdefaultencoding('utf-8')
get_datos(172)
#get_legislaturas(48)
#for m in boletines:
#	id_votacion(m,802)

#get_boletin(3482)
#id_votacion(4104)
#id_votacion(3270, 177)
#id_votacion(3844)
#id_votacion(3844)
#print boletines