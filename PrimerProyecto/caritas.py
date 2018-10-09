# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 00:24:27 2018

@author: La Banda Gangrena
"""
import pandas as pd
import json
import matplotlib.pyplot as plt

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

collEst = db.estaciones
collBic = db.bicis
#Para graficar atributos promedio de estaciones agrupando por código postal:
cp = {} #Mapeo de id de estación a código postal
edad = {} #Edad promedio de los usuarios
genero = {} #Género "promedio" de los usuarios
viajes = {} #Cantidad promedio de viajes al día
distancia = {} #Longitud promedio de recorridos al día
hora = {} #Hora pico promedio 
for doc in collEst.find({},{"_id":0,"id":1, "zip":1}):
    est = doc["id"]
    codigo = doc["zip"]
    if codigo in cp:
        cp[codigo].append(est)
    else:
        cp[codigo] = [est]


