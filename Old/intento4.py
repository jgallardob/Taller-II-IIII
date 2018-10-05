#-*- coding: utf-8 -*-
#Script 3 Datos diputados
#Ejemplo con un Diputado
#Codigo Diputado 915

import bs4 as BS 
import urllib2
import sys
import csv

cod_diputados = []
diputado = []
def get_pid():
	url = "http://opendata.camara.cl/wscamaradiputados.asmx/getDiputados_Vigentes"
	source = urllib2.urlopen(url).read()
	soup   = BS.BeautifulSoup(source, 'lxml')
	for lis in soup.find_all('diputado'):
		codigo = lis.find('dipid').text
		cod_diputados.append(codigo)
	return cod_diputados

def get_votaciones(dato):
	id_diputado = int(dato)
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
		diputado = []
reload(sys)
sys.setdefaultencoding('utf-8')
get_pid()
for i in cod_diputados:
	get_votaciones(i)