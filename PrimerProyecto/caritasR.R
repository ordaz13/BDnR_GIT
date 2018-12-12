install.packages("aplpack")
library(aplpack)
datos <- read.csv('datos.csv')

plotdat <- matrix(1,nrow=31,ncol=15) # all constant
#rownames(plotdat)<- c("Distancia","Horas", "Genero", "Edad", "Viajes")
# now set only the columns aka face components of interest
#plotdat[,2]<-datos$Colonia
plotdat[,1]<-datos$Distancia
plotdat[,11]<-datos$Horas
plotdat[,9]<-datos$Genero
plotdat[,6]<-datos$Edad
plotdat[,8]<-datos$Viajes

faces(plotdat,face.type=1,scale = TRUE,cex=0.85,print.info = TRUE, labels = datos$Colonia)
