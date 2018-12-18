from pymongo import MongoClient
from pprint import pprint
import csv


def conex(collect):
    return collect.find()

def maximo(m):
    Max = 0
    for a in m:
        if len(a) > Max:
            Max = len(a)
    for arr in m:
        while len(arr) < Max:
            arr.append("7")

def toCSV(m):
    spamWriter = csv.writer(open('Votaciones_Llenadas_Legislatura Actual.csv', 'wb'), delimiter=',', quotechar=',',
                        quoting=csv.QUOTE_MINIMAL)
    for fila in m:
        spamWriter.writerow(fila)



client = MongoClient("localhost", 27017)
db = client.oscuridad
cursor = conex(db.legis)
cursorp = conex(db.parlamentario)

Dip=[]
for datap in cursorp:
    Dip.append([datap["_id"].encode("utf-8"),datap["nombre"].encode("utf-8"),datap["partido"].encode("utf-8")])

votosf = []
for data in cursor:
    for sesion in data["50"]["sesiones"]:
        for boletines in sesion["boletines"]:
            for proyectos in boletines["proyectos"]:
                for data in proyectos["votaciones"]:
                    try:
                        votosf.append([data["Id_Diputado"], data["voto"]])
                    except:
                        print "ERROR"

for i in range(len(Dip)):
    for j in range(len(votosf)):
        if(Dip[i][0]==votosf[j][0]):
            Dip[i].append(votosf[j][1])
maximo(Dip)
toCSV(Dip)
