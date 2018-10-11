#install.packages("aplpack")
datos <- read.csv('datos.csv')
library(aplpack)
faces(datos[,3:7])

plotdat <- matrix(runif(15*31),nrow=31,ncol=15) # all constant
#rownames(plotdat)<- c("Distancia","Horas", "Genero", "Edad", "Viajes")
# now set only the columns aka face components of interest
#plotdat[,2]<-datos$Colonia
plotdat[,3]<-datos$Distancia
plotdat[,4]<-datos$Horas
plotdat[,5]<-datos$Genero
plotdat[,6]<-datos$Edad
plotdat[,7]<-datos$Viajes

faces(plotdat,face.type=1,scale = TRUE,cex=0.85,print.info = TRUE, labels = datos$Colonia)
