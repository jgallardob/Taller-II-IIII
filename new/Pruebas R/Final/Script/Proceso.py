import json
import codecs
import rpy2.robjects as robjects
from rpy2.robjects.packages import importr
#IMPORT LIBRARIES
wnom = importr('wnominate')
r = robjects.r
class Procesamiento:
    def __init__(self,ruta):
        self.ruta = ruta
        self.file= r['read.csv'](self.ruta, encoding='utf-8')
    def Matrix_Votaciones(self):
        votaciones =r['as.matrix'](self.file).rx(True,-1).rx(True,-1).rx(True,-1) #Quitar 3 Columnas
        return votaciones

    def Info_Parlament(self):
        iD = r['matrix'](self.file.rx(True,1))  #Rescatar Columna de iD
        nombre = r['matrix'](self.file.rx(True,2)) #Rescatar Columna de nombres
        partido = r['matrix'](self.file.rx(True,3)) # #Rescatar Columna de partidos
        return iD,nombre,partido

    def RC(self):
        #FORMAT WNOMINATE
        rc = r.rollcall(self.Matrix_Votaciones(), yea = [1,2,3], nay = [4,5,6],
                        missing = [7,8,9], notInLegis = 0,)
        result = wnom.wnominate(rc,polarity=robjects.IntVector((1,49)),minvotes = 10)
        #rescatar Coordenadas
        cx = result[0][6]
        cy = result[0][7]
        return result,cx,cy

    def Armar_Json(self,iD,nombres,partidos,x,y):
        #CREATE AND EXPORTATION ARCHIVE JSON
        objects = {}
        objects['Legislatura'] = []
        for object in range(len(nombres)):
            objects['Legislatura'].append(
            {
                'Id_P':''+str(iD[object])+'',
                'Nombre': ''+ nombres[object]+'',
                'Partido': ''+partidos[object]+'',
                'X': ''+str(x[object])+'',
                'Y': ''+str(y[object])+''
                })
        return objects
