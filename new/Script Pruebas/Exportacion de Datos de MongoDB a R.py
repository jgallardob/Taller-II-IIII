import csv
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.final
data_collection = [db.sesion, db.votacion, db.parlamentario, db.proyecto]


def get_all_data(x):
    coleccion = data_collection[x]
    conex = coleccion.find()
    return conex


def get_data(field, value, x):
    coleccion = data_collection[x]
    conex = coleccion.find({field: value})
    return conex


def get_votaciones_proyecto(proyecto, diputado, db):
    coleccion = data_collection[db]
    conex = coleccion.find({"$and": [{"Id": proyecto}, {"Id_Diputado": diputado}]})
    return conex


ids_diputados = []

nFh = open("Votaciones x n-Proyectos", "w")

# obteniendo una lista de todos los diputados vigentes
lista_diputados = get_all_data(2)
for data in lista_diputados:
    ids_diputados.append(data["_id"])
ids_diputados = list(set(ids_diputados))
ids_diputados.sort()
# -------------------------------------------------------

for i in range(len(ids_diputados)):
    datos_diputado = get_data("_id", ids_diputados[i], 2)
    for datos in datos_diputado:
        nFh.write(datos["_id"] + " ")
        nFh.write(datos["nombre"].encode('utf-8') + " ")
        nFh.write(datos["partido"].encode('utf-8') + " ")

    proyectos = get_all_data(3)
    ids_Votaciones = []
    votoXdiputado = []
    # aqui saco todas los ids de votaciones que hay en la coleccion proyecto
    for votaciones in proyectos:
        ids_Votaciones.append(votaciones["id_votacion"])
    # y se guardan en un areglo
    # en donde solo ocupo 10 ids de votacion
    for j in range(len(ids_Votaciones[0:25])):
        id_votacion = get_votaciones_proyecto(ids_Votaciones[j], ids_diputados[i], 1)
        for data in id_votacion:
            nFh.write(data["voto"] + " ")
    nFh.write("\n")

nFh.close()

nFh = open("Votaciones x nProyectos", "r")
matrix = []
linea = nFh.readlines()
for info in linea:
    matrix.append(info[:-2].split(" "))
client.close()

spamWriter = csv.writer(open('votaciones_.csv', 'wb'), delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL)
for fila in matrix:
    spamWriter.writerow(fila)
