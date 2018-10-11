# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 00:24:27 2018

@author: La Banda Gangrena
"""
import pandas as pd
import json
import matplotlib.pyplot as plt
from math import sin, cos, sqrt, asin, pi
from pylab import *

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

#Declaración de variables globales
collEst = db.estaciones
collBic = db.bicis
#Para graficar atributos promedio de estaciones agrupando por código postal:
#Obtención de datos
cp = {} #Mapeo de id de estación a código postal
edad = {} #Edad promedio de los usuarios
genero = {} #Género "promedio" de los usuarios
viajes = {} #Cantidad promedio de viajes al día
distancia = {} #Longitud promedio de recorridos al día
hora = {} #Hora pico promedio 
c = pi/180 #Constante para transformar de radianes a grados

#Función para obtener datos
def obtiene_datos():
    for codigo in cp:
        ed = 0 #edad
        g = 0 #género
        v = 0 #número de viajes
        d = 0 #distancia recorrida
        horas = {} 
        for clave in cp[codigo]:
            for doc in collBic.find({"Ciclo_Estacion_Retiro":clave},{"Edad_Usuario":1, "Genero_Usuario":1, "Ciclo_Estacion_Arribo":1}):
                destino = doc["Ciclo_Estacion_Arribo"]
                if destino == 111 or destino == 103 or destino > 446:
                    continue
                ed = ed + doc["Edad_Usuario"]
                g = g + 1 if doc["Genero_Usuario"]=='F' else g - 1
                v = v + 1
                inicioLon = collEst.find({"id":clave},{"_id":0,"lon":1}).limit(1)[0]["lon"]
                inicioLat = collEst.find({"id":clave},{"_id":0,"lat":1}).limit(1)[0]["lat"]
                finLon = collEst.find({"id":destino},{"_id":0,"lon":1}).limit(1)[0]["lon"]
                finLat = collEst.find({"id":destino},{"_id":0,"lat":1}).limit(1)[0]["lat"]
                d = d + (2*6367.45*asin(sqrt(sin(c*(finLat-inicioLat)/2)**2+cos(c*inicioLat)*cos(c*finLat)*sin(c*(finLon-inicioLon)/2)**2)))
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
            #obtener datos de distancias
            ed = ed/v
            v = v/len(cp[codigo])
            d = d/v
            edad[codigo] = ed
            genero[codigo] = g
            viajes[codigo] = v
            distancia[codigo] = d
            hora[codigo] = max(horas.values())/v
"""
        
#Función para normalizar datos de una lista
def normaliza(x): 
    maxx = max(x)
    minx = min(x)
    for i in range(len(x)):
        x[i] = (x[i]-minx)/(maxx-minx)
        if x[i] < 0.001:
            x[i] = 0.001
    return x

#Funcion para dejar los datos entre 1 y 7
def datos_17(x):
    maxx = max(x)
    minx = min(x)
    for i in range(len(x)):
        x[i] = ((7-1)/(maxx-minx))*(x[i]-maxx)+7
    return x

#Función para graficar las caritas de Chernoff
def cface(ax, x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18):
    # x1 = height  of upper face
    # x2 = overlap of lower face
    # x3 = half of vertical size of face
    # x4 = width of upper face
    # x5 = width of lower face
    # x6 = length of nose
    # x7 = vertical position of mouth
    # x8 = curvature of mouth
    # x9 = width of mouth
    # x10 = vertical position of eyes
    # x11 = separation of eyes
    # x12 = slant of eyes
    # x13 = eccentricity of eyes
    # x14 = size of eyes
    # x15 = position of pupils
    # x16 = vertical position of eyebrows
    # x17 = slant of eyebrows
    # x18 = size of eyebrows

    # top of face, in box with l=-x4, r=x4, t=x1, b=x3
    e = mpl.patches.Ellipse( (0,(x1+x3)/2), 2*x4, (x1-x3), fc='white', linewidth=2)
    ax.add_artist(e)

    # bottom of face, in box with l=-x5, r=x5, b=-x1, t=x2+x3
    e = mpl.patches.Ellipse( (0,(-x1+x2+x3)/2), 2*x5, (x1+x2+x3), fc='white', linewidth=2)
    ax.add_artist(e)

    # cover overlaps
    e = mpl.patches.Ellipse( (0,(x1+x3)/2), 2*x4, (x1-x3), fc='white', ec='none')
    ax.add_artist(e)
    e = mpl.patches.Ellipse( (0,(-x1+x2+x3)/2), 2*x5, (x1+x2+x3), fc='white', ec='none')
    ax.add_artist(e)
    
    # draw nose
    plot([0,0], [-x6/2, x6/2], 'k')
    
    # draw mouth
    p = mpl.patches.Arc( (0,-x7+.5/x8), 1/x8, 1/x8, theta1=270-180/pi*arctan(x8*x9), theta2=270+180/pi*arctan(x8*x9), facecolor='black')
    ax.add_artist(p)
    
    # draw eyes
    p = mpl.patches.Ellipse( (-x11-x14/2,x10), x14, x13*x14, angle=-180/pi*x12, facecolor='white')
    ax.add_artist(p)
    
    p = mpl.patches.Ellipse( (x11+x14/2,x10), x14, x13*x14, angle=180/pi*x12, facecolor='white')
    ax.add_artist(p)

    # draw pupils
    p = mpl.patches.Ellipse( (-x11-x14/2-x15*x14/2, x10), .05, .05, facecolor='black')
    ax.add_artist(p)
    p = mpl.patches.Ellipse( (x11+x14/2-x15*x14/2, x10), .05, .05, facecolor='black')
    ax.add_artist(p)
    
    # draw eyebrows
    plot([-x11-x14/2-x14*x18/2,-x11-x14/2+x14*x18/2],[x10+x13*x14*(x16+x17),x10+x13*x14*(x16-x17)],'k')
    plot([x11+x14/2+x14*x18/2,x11+x14/2-x14*x18/2],[x10+x13*x14*(x16+x17),x10+x13*x14*(x16-x17)],'k')
"""
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
#Obtiene datos y los pone en las variables globales
obtiene_datos()
"""
#Normaliza datos para graficar
edadValues = normaliza(list(edad.values()))
generoValues = normaliza(list(genero.values()))
horaValues = normaliza(list(hora.values()))
distanciaValues = normaliza(list(distancia.values()))
viajesValues = normaliza(list(viajes.values()))
#Grafica
fig = figure(figsize=(20,20))
for i in range(len(cp)):
    ax = fig.add_subplot(6,6,i+1,aspect='equal')
    #cface(ax, rand(), rand(), rand(), rand(), viajesValues[i], horaValues[i], rand(), distanciaValues[i], rand(), rand(), rand(), rand(), rand(), edadValues[i], rand(), rand(), generoValues[i], rand())
    cface(ax, *rand(18))
    ax.axis([-1.2,1.2,-1.2,1.2])
    ax.set_xticks([])
    ax.set_yticks([])

fig.subplots_adjust(hspace=0, wspace=0)


