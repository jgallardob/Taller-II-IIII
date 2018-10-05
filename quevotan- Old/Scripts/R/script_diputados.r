library(wnominate)

votaciones  		<- read.csv('../Data/source_r.csv', header=TRUE, strip.white=TRUE, encoding='UTF-8')
votaciones2 		<- as.matrix(votaciones[,-c(1:2)])
nombres     		<- matrix(votaciones[,1])
colnames(nombres)	<- "parlament"
partidos			<- matrix(votaciones[,2], length(votaciones[,2]),1)
colnames(partidos)	<- "party"
rc 					<- rollcall(votaciones2, yea = c(1,2,3), nay = c(4,5,6), missing = c(7,8,9), notInLegis = 0, legis.data = partidos, desc = "Diputados")
result				<- wnominate(rc, polarity = c(49,49), verbose = T, minvotes = 1000)
summary(result)
par(mfrow = c(1,1))
plot.coords(result)
write.table(result$legislators, file='../Data/out_r.csv', row.names_= TRUE, sep = ',')