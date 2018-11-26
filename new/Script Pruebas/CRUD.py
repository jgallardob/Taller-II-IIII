import pymongo
from pymongo import MongoClient
from pprint import pprint

print """
    0 --> datos de sesion
    1 --> datos de legislatura
    2 --> datos de proyecto
    3 --> datos de boletin
    4 --> datos de votacion
    5 --> datos de parlamentario
    6 --> datos de comision \n"""

#----Leer datos desde un txt---->
f=open("Diputados_new.txt","r")
info=f.readlines()
data=[]
for dato in info:
    data.append(dato.split(" "))
#----Conectarse a la BD mongo---->    
client=MongoClient('localhost',27017)
db=client.integracion
#----Arreglo con las colecciones de la BD---->
data_collection=[db.sesion,db.legislatura,db.proyecto,db.boletin,db.votacion,db.parlamentario,db.comision]
#----Funcion para ver los datos de una coleccion
def get_data(x):
    coleccion=data_collection[x]
    conex=coleccion.find()
    for dato in conex:
        pprint(dato)
        print "\n"
#----Funcion para consultar por campo y valor
def query(field, value, db_collect):
    coleccion=data_collection[db_collect]
    cursor=coleccion.find({field:value})
    for dato in cursor:
        pprint(dato)
    return cursor
#----Estructura de txt---->                                         
#[ID]  [NOMBRE]  [APELLIDO MATERNO]  [APPELIDO PATERNO]  
def insert_data_diputados(aDiputadoInfo, db):
    for data in aDiputadoInfo:
        db.insert({"id_parlamentario":data[0],"Nombre":data[1],"Apellido_Paterno":data[3][:-1],"Apellido_Materno":data[2]})






#----MAIN---->
#----Insercion de datos en coleccion PARLAMENTARIOS---->        
insert_data_diputados(data,data_collection[5])    
#----Consulta de los datos---->
while True:
    n=raw_input("Ingresa la opcion: ")
    if n=="salir":
        break
#----Obtener datos de una determinada coleccion---->
    get_data(int(n))

#----Cierre de la conexion con mongo---->
client.close()
