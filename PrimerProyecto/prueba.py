# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 20:01:41 2018

@author: La Banda Gangrena
"""

#import pandas as pd
#import json
#import sys
import matplotlib.pyplot as plt

#Hace conexion
from pymongo import MongoClient as Connection
connection = Connection('localhost',27017)
db = connection.ecobicis #Crea la base Ecobicis

"""
data = pd.read_csv('2018-01.csv') #Base de Enero  
data_json = json.loads(data.to_json(orient='records')) #Convierte de csv a json
db.bicis.insert_many(data_json) #Crea colleccion bicis e inserta datos json a mongo
"""

#Imprime todos los valores
coll = db.bicis
arrEdad = []
for doc in coll.find({},{"_id":0,"Edad_Usuario":1}):
    edad = doc["Edad_Usuario"]
    arrEdad.append(edad)
#print(arrEdad)
plt.figure()
plt.hist(arrEdad,bins=7,range=(18,80))
plt.title("Histograma de edades",size=15)
plt.xlabel("Edad en años")
plt.ylabel("Cantidad de personas")
#Recordar que clave única es bici + fechaRetiro + horaRetiro
