# -*- coding: utf-8 -*-
#Script Prueba encargado de extraer legistalturas y sesiones actuales y totales
#By Alfoso Duarte B

import requests
from bs4 import BeautifulSoup

def Get_Legislatura_Actual():
    Url_LegislaturaActual="http://opendata.camara.cl/camaradiputados/WServices/WSLegislativo.asmx/retornarLegislaturaActual?"
    r = requests.get(Url_LegislaturaActual)
    data = r.text
    soup = BeautifulSoup(data, 'xml')
    result = soup.find("Legislatura")
    LegislaturaActual = result.Id.text.encode('utf-8')
    return LegislaturaActual

def Get_Legislaturas():
    Legislaturas=[]
    Url_Legislaturas="http://opendata.camara.cl/camaradiputados/WServices/WSLegislativo.asmx/retornarLegislaturas?"
    r = requests.get(Url_Legislaturas)
    data = r.text
    soup = BeautifulSoup(data, 'xml')
    result = soup.find_all("Legislatura")
    for i in result:
        Legislaturas.append(i.Id.text.encode('utf-8'))
    return Legislaturas

def Get_SesionesxLegislaturaActual(leg):
    Sesiones=[]
    Url_Sesion="http://opendata.camara.cl/camaradiputados/WServices/WSSala.asmx/retornarSesionesXLegislatura?prmLegislaturaId="+str(leg)
    r = requests.get(Url_Sesion)
    data = r.text
    soup = BeautifulSoup(data, 'xml')
    result = soup.find_all("Sesion")

    f=open("Sesiones_legislatura_actual.txt","w")
    for i in result:
        try:
            f.write(i.Id.text.encode('utf-8')+ "\n")
        except IndexError, AttributeError:
            print "lol"
        print "procesando informacion....espere (:"
          
    f.close()
    print "Listo (: ### informacion guardada en Sesiones.txt ###"

def Get_SesionesxLegislatura(leg):
    legis = leg
    Sesiones=[]

    f=open("SesionesCompletas.txt","w")
    for i in legis:
        Url_Sesion="http://opendata.camara.cl/camaradiputados/WServices/WSSala.asmx/retornarSesionesXLegislatura?prmLegislaturaId="+str(i)
        r = requests.get(Url_Sesion)
        data = r.text
        soup = BeautifulSoup(data, 'xml')
        result = soup.find_all("Sesion")
        for i in result:
            Sesiones.append(i.Id.text.encode('utf-8'))
            print "Extrayendo informacion....espere"
    for i in Sesiones:
        f.write(i + "\n")          
    f.close()
    print "Listo (: ### informacion guardada en SesionesCompletas.txt ###"


if __name__ == "__main__": 
    Get_SesionesxLegislatura(Get_Legislaturas())
    Get_SesionesxLegislaturaActual(Get_Legislatura_Actual())
