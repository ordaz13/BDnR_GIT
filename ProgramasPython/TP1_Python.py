# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 16:54:46 2018
@author: usuario
"""
import random
#1.a Funcion para agregar ceros a un arreglo
def desplazaArreglo(a,k):
    aux = []
    if k > 0:
        for i in range(k):
            aux.append(0)
        a[0:k] = []
        for j in range(len(a)):
            aux.append(a[j])
        a = aux
    else:
        k = abs(k)
        a[len(a)-k:len(a)] = []
        for i in range(len(a)):
            aux.append(a[i])
        a = aux
        for j in range(k):
            a.append(0)
    return a
#1.b Funcion de la suma de matrices
def sumaMatrices(a,b):
    if len(a) == len(b):
        c = [[0]*len(a) for i in range(len(a))]
        for i in range(len(a)):
           for j in range(len(a[0])):
               c[i][j] = a[i][j] + b[i][j]
        return c
    else:
        return "No se puede realizar"
#2. Funcion del promedio ponderado
def promedioPond(calif):
    pond = [.10, .20, .23, .30, .17]
    prom = 0
    for i in range(len(calif)):
        if calif[i] >= 6:
            prom = prom + calif[i]*pond[i]
    return round(prom)
#2. Otra forma de hacer la función pasada es
def promedioPond2(calif):
    porcentajes = [.1,.2,.23,.3,.17]
    prom = [c*p for c,p in zip(calif, porcentajes)]
    result = round(sum(prom),1)
    return result
#3. Funcion que obtiene los pares de una lista
def tuplaPares(a):
    resp = []
    for i in range(0, len(a), 2):
        resp.append(a[i])
    return resp
#4. Funcion que verifica si hay elementos iguales
def superposicion(a,b):
    bandera = False
    for i in range(len(a)):
        if bandera == False:
            for j in range(len(b)):
                if bandera == False:
                    bandera = a[i] == b[j]
                else:
                    break
        else:
            break
    return bandera
 #5. Funcion que cuenta las repeticiones en una cadena
def repeticiones(cad):
    dic = {} 
    listaCad = cad.split()
    for j in listaCad:
        if j in dic:
            dic[j] = dic[j] + 1
        else:
            dic[j] = 1
    return dic
#6. Función que calcula las veces que una suma de dados dio lo mismo
def sumaDados(n):
    dic = {}
    for i in range(n):
        sum = random.randint(1,6) + random.randint(1,6)
        if sum in dic:
          dic[sum] = dic[sum] + 1
        else:
          dic[sum] = 1
    return dic
#6.1 Función que muestra los pares del lanzamiento
def paresDados(n):
    dic = {}
    for i in range(n):
        par1 = random.randint(1,6)
        par2 = random.randint(1,6)
        lanzamiento = par1, par2
        lanzamientoI = par2, par1
        if lanzamiento in dic or lanzamientoI in dic:
            if lanzamiento in dic:
                dic[lanzamiento] = dic[lanzamiento] + 1
            else:
                dic[lanzamientoI] = dic[lanzamientoI] + 1
        else:
            dic[lanzamiento] = 1
    return dic

##Prueba de la funcion desplazaArreglo
#a = [1,2,3,4,5,6]
#k = -3
#resp = desplazaArreglo(a,k)
##Prueba de la funcion del promedio ponderado
#calif = []
#for i in range(5):
#    calif.append(random.randint(6,10))
#prom = promedioPond(calif)
#prom2 = promedioPond2(calif)
##Prueba suma de matrices
#x = [[1,2,3], [4,5,6], [7 ,8,9]]
#y = [[9,8,7], [6,5,4], [3,2,1]]
#resp = sumaMatrices(x,y)
##Prueba de la funcion tuplaPares
#b = ['a','b','c','d']
#resp = tuplaPares(b)
##Prueba superposicion
#m = ['a','b','c','d']
#n = [1,2,3,4,5,6]
#resp = superposicion(m,n)
##Prueba repeticiones
#a = 'que día tan lluvioso que hace hoy'
#resul = repeticiones(a)
#print(resul)
##Prueba repeticiones
#n = 10
#resul = sumaDados(n)
#print(resul)
#Prueba pares
n = 10
resul = paresDados(n)
print(resul)