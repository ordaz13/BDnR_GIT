#Ejercicio del examen anterior
def ejercicioPy(archivoCambios, archivoDatos):
    archC = open(archivoCambios, 'r')
    cadC = archC.read()
    listaCadC = cadC.split('\n')
    archC.close()
    for palabra in listaCadC:
        elemento = palabra.split(',')
        busca = elemento[0]
        reemplaza = elemento[1]; reemplaza = reemplaza[1:]
        archD = open(archivoDatos,'r')
        cadD = archD.read()
        listaCadD = cadD.split('\n')
        archD.close()
        archD = open(archivoDatos, 'w')
        for linea in listaCadD:
            nuevaLinea = linea.replace(busca, reemplaza)
            archD.write(nuevaLinea+'\n')
        archD.close()
        
#Probamos el metodo
ejercicioPy('ArchivoCambios.txt','ArchivoDatos.txt')
            
