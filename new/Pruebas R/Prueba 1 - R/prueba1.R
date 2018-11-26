#Ejemplo 1
library(wnominate)
library(RJSONIO)
rm(list = ls(all = TRUE))  #Limpia los datos que se encuentra en la memoria
UN<- read.csv("source.csv", header = FALSE, strip.white = TRUE) #Lee el archivo csv
data(UN) #importa datos que se leyeron

dataUN <- as.matrix(UN) #Ingresa datos deto de un matriz
UN[1:5, 1:6]   #Muestrame las filas del 1 al 5 y columnas del 1 al 6
UNames <- UN[, 1]  #Muestrame la columna Nombres
legData <- matrix(UN[, 2], length(UN[, 2]), 1)  #Muestra partida Politico
colnames(legData) <- "party"  # Asigna Nombre a la Columna
UN <- UN[, - c(1, 2)]  #Retorna Votaciones

#Realiza Calculos
rc <- rollcall(UN, yea = c(1, 2, 3), nay = c(4, 5, 6), missing = c(7, 8, 9), notInLegis = 0, legis.names = UNames, legis.data = legData, desc = "UN Votes", source = "www.voteviwe.com")
result <- wnominate(rc, polarity = c(1, 1))
summary(result)
par(mfrow = c(1, 1))

#Exportar archivo en formato Json
exportJson <- toJSON(result)
write(exportJson,"Data_process.json")
plot(result)

