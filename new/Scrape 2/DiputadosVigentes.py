# -*- coding: utf-8 -*-
#Script Prueba encargado de extraer y filtrar informacion de cada Parlamentario Vigente
#By Alfoso Duarte B

import requests
import ctypes as ct
from bs4 import BeautifulSoup


DiputadosId = []; Diputados = []

def DiputadosVigentes():
    global DiputadosId

    Url_DipVigentes="http://opendata.camara.cl/camaradiputados/WServices/WSDiputado.asmx/retornarDiputadosPeriodoActual?"
    r = requests.get(Url_DipVigentes)
    data = r.text
    soup = BeautifulSoup(data, 'xml')
    result = soup.find_all("Diputado")

    for Dip in result:
        DiputadosId.append(Dip.Id.text)

def DiputadosDetalle():
    f=open("Diputados.txt","w")
    for i in DiputadosId:
        Url_Militancia = "http://opendata.camara.cl/camaradiputados/WServices/WSDiputado.asmx/retornarDiputado?prmDiputadoId="+str(i)
        #Url_Militancia = "http://opendata.camara.cl/wscamaradiputados.asmx/getDiputados_Vigentes" #url antigua caida ):
        r = requests.get(Url_Militancia)
        data = r.text
        soup = BeautifulSoup(data, 'xml')  
        result = soup.find ("Diputado")
        alias = soup.find_all("Alias")#se podria remplazar por Id de partido o nombre de partido

        try:
            f.write(str(i).encode('utf-8') +" "+ result.Nombre.text.replace(" ","-").encode('utf-8') +" "+ result.ApellidoPaterno.text.replace(" ","-").encode('utf-8') +" "+ alias[-1].text.encode('utf-8')+" "+ "\n")
        except IndexError, AttributeError:
            f.write(str(i).encode('utf-8') +" "+ result.Nombre.text.replace(" ","-").encode('utf-8') +" "+ result.ApellidoPaterno.text.replace(" ","-").encode('utf-8')+" "+ "\n" )
        print "procesando informacion....espere (:"
    f.close()
    print "Listo (: ### informacion guardada en Diputados.txt ###"


if __name__ == "__main__":    
    DiputadosVigentes()
    DiputadosDetalle()




