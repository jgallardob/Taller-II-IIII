import rpy2.robjects as robjects
##################################### Code R ###########################################

code = robjects.r("""
library(wnominate)
library(RJSONIO)
library(pscl)
votaciones  		<- read.csv('./data/PruebaP.csv', header=FALSE, strip.white=TRUE, encoding='UTF-8') #Lectura del fichero
votaciones2 		<- as.matrix(votaciones[,-c(1:2)]) #Excluye los nombres y partidos
nombres     		<- matrix(votaciones[,1]) #Rescata el nombre del parlamentario
colnames(nombres)	<- "Parlamentario" #Inicializa el nombre
partidos			<- matrix(votaciones[,2], length(votaciones[,2]),1) #Agrega al arreglo el nombre + partido
colnames(partidos)	<- "Partidos" #NOmbre de columnas

#RollCall -> Atacha el arreglo de los datos, indica un diccionario con valores y da un nombre de visualizacion
rc 					<- rollcall(votaciones2, yea = c(1,2,3), nay = c(4,5,6), missing = c(7,8,9), notInLegis = 0, legis.data = partidos, desc = "Diputados")

#Parsea el resultado usando wnominate, indica los valores de polaridad, y el minimo de votos para considerar en procesamiento
result				<- wnominate(rc, polarity = c(1,155), verbose = T, minvotes = 25)

#Muestra los resultados por pantalla
summary(result)
#Crea el Arreglo de Partidos para mostrar
par(mfrow = c(1,1))
#Plotea el resultado en las dimensiones XY del plano
plot.coords(result)
#Exporta valores a un archivo csv
write.table(result$legislators, file='./data/Procesado.csv', sep = ',')

#Exportar archivo en formato Json
exportJson <- toJSON(result)
write(exportJson,"./data/Procesado.json")
""")
print code
