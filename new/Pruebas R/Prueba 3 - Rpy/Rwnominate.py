import rpy2.robjects as robjects
from rpy2.robjects.packages import importr
r = robjects.r
wnom = importr('wnominate')
r = robjects.r
votaciones = r['read.csv']('./data/PP.csv', encoding='UTF-8')
votaciones2 =r['as.matrix'](votaciones).rx(True,-1).rx(True,-1)
nombres = r['matrix'](votaciones.rx(True,1))
partidos = r['matrix'](votaciones.rx(True,2))
rc = r.rollcall(votaciones2, yea = [1,2,3], nay = [4,5,6],
                missing = [7,8,9], notInLegis = 0,)
result =wnom.wnominate(rc,polarity=robjects.IntVector((1,58)),minvotes = 10)
r.summary(result)
r.par(mfrow = [1,1])
r['plot.coords'](result)


"""
library(wnominate)
votaciones  		<- read.csv('./data/PruebaP.csv', header=TRUE, strip.white=TRUE, encoding='UTF-8')
votaciones2 		<- as.matrix(votaciones[,-c(1:2)])
nombres     		<- matrix(votaciones[,1])
colnames(nombres)	<- "parlament"
partidos			<- matrix(votaciones[,2], length(votaciones[,2]),1)
colnames(partidos)	<- "party"
rc 					<- rollcall(votaciones2, yea = c(1,2,3), nay = c(4,5,6), missing = c(7,8,9), notInLegis = 0, legis.data = partidos, desc = "Diputados")
result				<- wnominate(rc, polarity = c(1,58), verbose = T, minvotes = 1)
summary(result)
par(mfrow = c(1,1))
plot.coords(result)
write.table(result$legislators, file='../Data/out_r.csv', row.names_= TRUE, sep = ',')
"""
