    # -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 20:01:41 2018
@author: Octavio Ordaz
"""

#Libreria para leer desde archivos csv
import pandas as pd
#Libreria para trabajar con documentos JSON
import json
#Libreria que ocupamos para graficar los resultados de las consultas
import matplotlib.pyplot as plt
#En la consola usar: %matplotlib auto para graficar en ventana nueva.

#Base de usuarios en el mes de enero 
data = pd.read_csv('2018-01.csv')  
#Convierte de csv a json
data_json = json.loads(data.to_json(orient='records'))
#Crea colleccion bicis e inserta datos json a mongo
db.bicis.insert_many(data_json) 

#Hace conexion entre Python y Mongo
from pymongo import MongoClient as Connection
connection = Connection('localhost',27017)
#Crea la base de datos Ecobicis
db = connection.ecobicis 
#Crea la colección bicis
coll = db.bicis

#Histograma de las edades de los usuarios
#Creamos una lista vacia para almacenar las edades de los usuarios
edades = []
#Selecciona cada una de las tuplas que la consulta devolvio
for doc in coll.find({},{"_id":0,"Edad_Usuario":1}):
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

#Grafica de la cantidad de usuarios al día
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
    cantidad.append(coll.find({"Fecha_Retiro":fecha},{":id":0,"Bici":1}).count())
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