import time as dt

data = open("./Data/completa.csv","r")
for linea in data:
    line = linea.split(',')
    largo = len(line)
    #sprint linea,"\n"
    print largo
    dt.sleep(0.5)
