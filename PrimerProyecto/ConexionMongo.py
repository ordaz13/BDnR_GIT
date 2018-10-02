import pandas as pd
import json
import sys

#Hace conexion
from pymongo import MongoClient as Connection
connection = Connection('localhost',27017)
db = connection.ecobicis #Crea la base Ecobicis

data = pd.read_csv('2018-01.csv') #Base de Enero  
data_json = json.loads(data.to_json(orient='records')) #Convierte de csv a json
db.bicis.insert_many(data_json) #Crea colleccion bicis e inserta datos json a mongo

#Imprime todos los valores
coll = db.bicis
for doc in coll.find():
    print(doc)
    
#Recordar que clave única es bici + fechaRetiro + horaRetiro