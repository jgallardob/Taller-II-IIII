from Script import Proceso as p
import json
import rpy2.robjects as robjects
from rpy2.robjects.packages import importr
imjson = importr('RJSONIO')
r = robjects.r
#-------------------------------------------------------------------
#               Llamada a Metodos de la clase Procesamiento
#-------------------------------------------------------------------
def main():

    rutaq = './Data/completa.csv'
    aData = p.Procesamiento(rutaq)
    votaciones = aData.Matrix_Votaciones()
    iD,nombres,partidos = aData.Info_Parlament()
    result,x,y = aData.RC()
    objects = aData.Armar_Json(iD,nombres,partidos,x,y)
    #---------------------------------------------------
    #Exportar Coordenadas
    #---------------------------------------------------
    with open('./Data/Coord.json', 'w') as file:
        json.dump(objects, file, encoding='latin1')
    #--------------------------------------------------
    #Exportar analisis estadistico completo.
    #--------------------------------------------------
    djson = imjson.toJSON(result)
    r['write'](djson,"./Data/full.json")
    r['plot.coords'](result)

    #print votaciones
    for i in range(len(iD)):
        print str(iD[i])+" "+nombres[i]+" "+partidos[i]+" ",x," ",y
#-------------------------------------------------------------------------
#               Inicio del main
#-------------------------------------------------------------------------
if __name__ == '__main__':
    main()
