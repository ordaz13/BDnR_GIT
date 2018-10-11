# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 00:24:27 2018

@author: La Banda Gangrena
"""
import pandas as pd
import json
from math import sin, cos, sqrt, asin, pi
import csv

"""
#Hace conexion
from pymongo import MongoClient as Connection
connection = Connection('localhost',27017)
db = connection.ecobicis #Crea la base Ecobicis


data = pd.read_csv('estaciones.csv') #Base de estaciones
data_json = json.loads(data.to_json(orient='records')) #Convierte de csv a json
db.estaciones.insert_many(data_json) #Crea colleccion bicis e inserta datos json a mongo
data = pd.read_csv('2018-01.csv') #Base de bicis
data_json = json.loads(data.to_json(orient='records'))
db.bicis.insert_many(data_json)
"""

#Declaración de variables
collEst = db.estaciones
collBic = db.bicis
c = pi/180 #Constante para transformar de radianes a grados
#Variables para almacenar atributos promedio de estaciones agrupando por código postal (colonia):
cp = {} #Mapeo de id de estación a código postal
edad = {} #Edad promedio de los usuarios
genero = {} #Género "promedio" de los usuarios
viajes = {} #Cantidad promedio de viajes al día
distancia = {} #Longitud promedio de recorridos al día
hora = {} #Hora pico promedio 

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
        hora[codigo] = max(horas.values())/v
        
#Manda valores de las consultas a un archivo csv para usarlo en R
i = 1
with open('datos.csv','w') as archivo:
    fila = csv.writer(archivo)
    fila.writerow(['Num', 'CP', 'Colonia', 'Distancia', 'Horas', 'Genero', 'Edad', 'Viajes'])
    for codigo in cp:
        fila.writerow([i, codigo, 'Colonia', distancia[codigo], hora[codigo], genero[codigo], edad[codigo], viajes[codigo]])
        i = i + 1
archivo.close()


