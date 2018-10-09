# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 20:01:41 2018
@author: Octavio Ordaz
"""

"""
import pandas as pd
import json

#Base de Enero 
data = pd.read_csv('2018-01.csv')  
#Convierte de csv a json
data_json = json.loads(data.to_json(orient='records'))
#Crea colleccion bicis e inserta datos json a mongo
db.bicis.insert_many(data_json) 
"""

import matplotlib.pyplot as plt
#En la consola usar: %matplotlib auto para graficar en ventana nueva.

#Hace conexion
from pymongo import MongoClient as Connection
connection = Connection('localhost',27017)
#Crea la base Ecobicis
db = connection.ecobicis 
#Crea la colección bicis
coll = db.bicis

#Histograma de las edades de los usuarios
edades = []
for doc in coll.find({},{"_id":0,"Edad_Usuario":1}):
    edades.append(doc["Edad_Usuario"])
#print(arrEdad)
plt.figure()
plt.hist(edades,bins=10,range=(18,80))
plt.title("Histograma de edades",size=15)
plt.xlabel("Edad en años")
plt.ylabel("Cantidad de personas")

#Grafica de la cantidad de usuarios al día
fechaRetiro = []
cantidad = []
for i in range(1,32):
    if i < 10:
        fecha = "0"+str(i)+"/01/2018"
    else:
        fecha = str(i)+"/01/2018"
    fechaRetiro.append(fecha)
    cantidad.append(coll.find({"Fecha_Retiro":fecha},{":id":0,"Bici":1}).count())
plt.figure()
plt.bar(fechaRetiro,cantidad)
plt.title("Cantidad de usuarios al día",size=15)
plt.xlabel("Fecha")
plt.xticks(rotation=90)
plt.ylabel("Cantidad de usuarios")


