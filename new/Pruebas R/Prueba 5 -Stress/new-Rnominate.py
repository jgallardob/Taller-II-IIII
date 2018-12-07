import json
import codecs
import rpy2.robjects as robjects
from rpy2.robjects.packages import importr

#IMPORT LIBRARIES
wnom = importr('wnominate')
imjson = importr('RJSONIO')
r = robjects.r

#READ ARCHIVE
votaciones = r['read.csv']('./Data/nSalida.csv', encoding='utf-8')
votaciones2 =r['as.matrix'](votaciones).rx(True,-1).rx(True,-1).rx(True,-1) #Quitar 3 Columnas

#SAVE DATA
iD = r['matrix'](votaciones.rx(True,1))  #Rescatar Columna de iD
nombres = r['matrix'](votaciones.rx(True,2)) #Rescatar Columna de nombres
partidos = r['matrix'](votaciones.rx(True,3)) # #Rescatar Columna de partidos

#FORMAT WNOMINATE
rc = r.rollcall(votaciones2, yea = [1,2,3], nay = [4,5,6],
                missing = [7,8,9], notInLegis = 0,)
#Inicio de Calculos
result = wnom.wnominate(rc,polarity=robjects.IntVector((1,90)),minvotes = 10)
#Muestra Resultados
sum =r.summary(result)

#rescatar Coordenadas
cx = result[0][6]
cy = result[0][7]

#CREATE AND EXPORTATION ARCHIVE JSON
objects = {}
objects['Legislatura'] = []
for object in range(len(nombres)):
    objects['Legislatura'].append(
    {
        'Id_P':''+str(iD[object])+'',
        'Nombre': ''+ nombres[object]+'',
        'Partido': ''+partidos[object]+'',
        'X': ''+str(cx[object])+'',
        'Y': ''+str(cy[object])+''
        })
with open('./Data/Datos.json', 'w') as file:
    json.dump(objects, file, encoding='latin1')
