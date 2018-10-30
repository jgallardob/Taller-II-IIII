#Extraccion de datos en forma de objetos para facilitar la insercion a MongoDB

from parlamentarios import Diputado

for diputados in Diputado.getParlamentarios():
    print diputados #Cambiar por subir a DB
