 # -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 20:01:41 2018
@author: Octavio Ordaz y Amanda Velasco
"""
#---------------------Librerias-------------------------------------#
#Libreria para leer desde archivos csv
import pandas as pd
#Libreria para trabajar con documentos JSON
import json
#Libreria que ocupamos para graficar los resultados de las consultas
import matplotlib.pyplot as plt
#En la consola usar: %matplotlib auto para graficar en ventana nueva.
#Libreria para operaciones matemáticas
from math import sin, cos, sqrt, asin, pi
#Librería para escribir y leer archivos csv
import csv
#------------------------------------------------------------------#

#---------------------Conexion-------------------------------------#
#Hace conexion entre Python y Mongo
from pymongo import MongoClient as Connection
connection = Connection('localhost',27017)
#Crea la base de datos Ecobicis
db = connection.ecobicis 
#------------------------------------------------------------------#

#-----------------Importa datos a base en mongo--------------------#
#Base de usuarios en el mes de enero 
data = pd.read_csv('2018-01.csv')  
#Convierte de csv a json
data_json = json.loads(data.to_json(orient='records'))
#Crea coleccion bicis e inserta datos json a mongo
db.bicis.insert_many(data_json) 
#Base de cicloestaciones
data = pd.read_csv('estaciones.csv')
#Convierte de csv a json
data_json = json.loads(data.to_json(orient='records'))
#Crea coleccion estaciones e inserta datos json a mongo
db.estaciones.insert_many(data_json) #Crea colleccion bicis e inserta datos json a mongo
#------------------------------------------------------------------#

#-------------------------Crea colecciones-------------------------#
#Crea la colección bicis
collBic = db.bicis
collEst = db.estaciones
#------------------------------------------------------------------#

#--------------Histograma de las edades de los usuarios------------#
#Creamos una lista vacia para almacenar las edades de los usuarios
edades = []
#Selecciona cada una de las tuplas que la consulta devolvio
for doc in collBic.find({},{"_id":0,"Edad_Usuario":1}):
#Del documento selecciona el valor que esta en el campo de "Edad_Usuario"
    edades.append(doc["Edad_Usuario"])
#Crea una nueva ventana para graficar
plt.figure()
#Grafica un histograma para los valores de las edades en grupos de 10
plt.hist(edades,bins=10,range=(18,80))
#Titulo de la grafica
plt.title("Histograma de edades",size=15)
#Añade etiquetas a los ejes
plt.xlabel("Edad en años")
plt.ylabel("Cantidad de personas")
#------------------------------------------------------------------#

#----------Grafica de la cantidad de usuarios al dia---------------#
#Crea listas vacias para almacenar las fechas y la cantidad de usuarios
fechaRetiro = []
cantidad = []
#Ciclo que representa los dias del mes de enero
for i in range(1,32):
#Generamos la fecha por buscar dentro de la consulta
    if i < 10:
        fecha = "0"+str(i)+"/01/2018"
    else:
        fecha = str(i)+"/01/2018"
#Guarda la fecha en la lista
    fechaRetiro.append(fecha)
#Guarda en la lista la cuenta de los usuarios registrados en esa fecha
    cantidad.append(collBic.find({"Fecha_Retiro":fecha},{":id":0,"Bici":1}).count())
#Crea una nueva ventana para graficar
plt.figure()
#Hace una grafica de dispersión de la cantidad de usuarios por fecha
plt.plot(fechaRetiro,cantidad,'bo',fechaRetiro,cantidad,'b')
#Titulo de la grafica
plt.title("Cantidad de usuarios al día",size=15)
#Añade etiquetas a los ejes, pone las etiquetas del eje x rotadas verticalmente 
plt.xlabel("Fecha")
plt.xticks(rotation=90)
plt.ylabel("Cantidad de usuarios")
#Activa las lineas de la grafica
plt.grid(True)
#------------------------------------------------------------------#

#-------Obtiene datos para graficar caras de Chernoff--------------#
#Obtiene datos para graficar caras de Chernoff
#Declaración de variables
c = pi/180 #Constante para transformar de radianes a grados
#Variables para almacenar atributos promedio de estaciones agrupando por código postal (colonia):
cp = {} #Mapeo de id de estación a código postal
edad = {} #Edad promedio de los usuarios
genero = {} #Género "promedio" de los usuarios
viajes = {} #Cantidad promedio de viajes al día
distancia = {} #Longitud promedio de recorridos al día
hora = {} #Hora pico

#Hace el mapeo de todas las cicloestaciones a su código postal correspondiente
for doc in collEst.find({},{"_id":0,"id":1, "zip":1}):
    if doc["id"] is None or doc["zip"] is None:
        continue
    est = int(doc["id"])
    codigo = int(doc["zip"])
    if codigo in cp:
        cp[codigo].append(est)
    else:
        cp[codigo] = [est]

#Obtiene datos
for codigo in cp:
    ed = 0 #edad
    g = 0 #género
    v = 0 #número de viajes
    d = 0 #distancia recorrida
    horas = {} 
    for clave in cp[codigo]:
        for doc in collBic.find({"Ciclo_Estacion_Retiro":clave},{"Edad_Usuario":1, "Genero_Usuario":1, "Ciclo_Estacion_Arribo":1}):
            destino = doc["Ciclo_Estacion_Arribo"]
            if destino == 111 or destino == 103 or destino > 446: #Datos insuficientes para estas estaciones
                continue
            ed = ed + doc["Edad_Usuario"]
            g = g + 1 if doc["Genero_Usuario"]=='F' else g - 1
            v = v + 1
            #Calcula la distancia de un viaje usando la fórmula de Haversine
            inicioLon = collEst.find({"id":clave},{"_id":0,"lon":1}).limit(1)[0]["lon"]
            inicioLat = collEst.find({"id":clave},{"_id":0,"lat":1}).limit(1)[0]["lat"]
            finLon = collEst.find({"id":destino},{"_id":0,"lon":1}).limit(1)[0]["lon"]
            finLat = collEst.find({"id":destino},{"_id":0,"lat":1}).limit(1)[0]["lat"]
            d = d + (2*6367.45*asin(sqrt(sin(c*(finLat-inicioLat)/2)**2+cos(c*inicioLat)*cos(c*finLat)*sin(c*(finLon-inicioLon)/2)**2)))
        #Cuenta frecuencia de viajes por hora
        for i in range(0, 24):
            menor = str(i) + ":00:00"
            mayor = str(i+1) + ":00:00"
            if len(menor) < 8:
                menor = "0"+menor
            if len(mayor) < 8:
                mayor = "0"+mayor
            frec = collBic.find({"Hora_Retiro":{"$gte":menor, "$lt":mayor},"Ciclo_Estacion_Retiro":clave},{"_id":1}).count()
            if i in horas:
                horas[i] = horas[i] + frec
            else:
                horas[i] = frec
        ed = ed/v
        v = v/len(cp[codigo])
        d = d/v
        edad[codigo] = ed
        genero[codigo] = g
        viajes[codigo] = v
        distancia[codigo] = d
        aux = max(horas.values())
        for clave in horas:
            if horas[clave] == aux:
                hora[codigo] = clave
                break
        
#Manda valores de las consultas a un archivo csv para usarlo en R
i = 1
with open('datos.csv','w') as archivo:
    fila = csv.writer(archivo)
    fila.writerow(['Num', 'CP', 'Colonia', 'Distancia', 'Horas', 'Genero', 'Edad', 'Viajes'])
    for codigo in cp:
        fila.writerow([i, codigo, 'Colonia', distancia[codigo], hora[codigo], genero[codigo], edad[codigo], viajes[codigo]])
        i = i + 1
archivo.close()
#------------------------------------------------------------------#
