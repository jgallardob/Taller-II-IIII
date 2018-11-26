import json
import codecs
import rpy2.robjects as robjects
from rpy2.robjects.packages import importr

#IMPORT LIBRARIES
wnom = importr('wnominate')
imjson = importr('RJSONIO')
r = robjects.r

#READ ARCHIVE
votaciones = r['read.csv']('./data/nSalida.csv', encoding='utf-8')
votaciones2 =r['as.matrix'](votaciones).rx(True,-1).rx(True,-1).rx(True,-1)
print votaciones2
#SAVE DATA
iD = r['matrix'](votaciones.rx(True,1))
nombres = r['matrix'](votaciones.rx(True,2))
partidos = r['matrix'](votaciones.rx(True,3))

#FORMAT WNOMINATE
rc = r.rollcall(votaciones2, yea = [1,2,3], nay = [4,5,6],
                missing = [7,8,9], notInLegis = 0,)
print rc
result = wnom.wnominate(rc,polarity=robjects.IntVector((1,5)),minvotes = 10)
#print result
sum =r.summary(result)
par=r.par(mfrow = [1,1])
print par
cx = result[0][6]
cy = result[0][7]

#CREATE AND EXPORTATION ARCHIVE JSON
objects = {}
objects['Legislatura'] = []
for object in range(len(nombres)):
    objects['Legislatura'].append(
    {
        'Id_P':''+str(object)+'',
        'Nombre': ''+ nombres[object]+'',
        'Partido': ''+partidos[object]+'',
        'X': ''+str(cx[object])+'',
        'Y': ''+str(cy[object])+''
        })
with open('./data/Datos.json', 'w') as file:
    json.dump(objects, file, encoding='latin1')
print "objects"
