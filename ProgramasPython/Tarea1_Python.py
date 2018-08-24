# -*- coding: utf-8 -*-
"""
Avance la tarea 1 de Python
Created on Thu Aug 23 22:07:15 2018

@author: Octavio Ordaz
"""
#1.
def multiplicacionMatrices(a,b):
    if len(a[0]) == len(b):
        bT = [list(aux) for aux in zip(*b)]
        c = [[0]*len(b[0]) for i in range(len(a))]
        for i in range(len(a)):
            for j in range(len(bT)):
                c[i][j] = sum([a*b for a,b in zip(a[i],bT[j])])
        return c
    else: 
        return "No es posible hacer la multiplicacion"
    
#2.
def opPolinomios():
    arch = open('Polinomios.txt','r')
    cad = arch.read()
    listaCad = cad.split('\n')
    arch.close()
    pol1 = listaCad[0]; pol1 = pol1.split(' '); pol1 = pol1[0:-2]
    coef1 = pol1[0:len(pol1):2]; exp1 = pol1[1:len(pol1):2]
    pol2 = listaCad[1]; pol2 = pol2.split(' '); pol2 = pol2[0:-2]
    coef2 = pol2[0:len(pol2):2]; exp2 = pol2[1:len(pol2):2]
    #suma
    sumP1 = [0 for i in range(16)]
    for i in range(len(coef1)):
        sumP1[int(exp1[i])] = float(coef1[i])
    sumP2 = [0 for i in range(16)]
    for j in range(len(coef2)):
        sumP2[int(exp2[j])] = float(coef2[j])
    suma = [p1+p2 for p1,p2 in zip(sumP1, sumP2)]
    #multiplicacion
    #FALTA TERMINAR ESTA PARTE
    return suma
    
#3. 
def subCadena(stri,cad):
    pos = []
    for i in range(len(stri)):
        if stri[i] == cad[0]:
            pos.append(i)
    cuenta = 0
    for j in range(len(pos)):
        aux = stri[pos[j]:pos[j]+len(cad)]
        if aux == cad:
            cuenta = cuenta + 1
    return cuenta

#4. 
def repeticionesArchivo():
    arch = open('Palabras.txt','r')
    cad = arch.read()
    listaCad = cad.split('\n')
    arch.close()
    dic = {} 
    for j in listaCad:
        if j in dic:
            dic[j] = dic[j] + 1
        else:
            dic[j] = 1
    return dic

##1. Prueba
#A = [[1,2],[3,4]]
#B = [[1,2],[3,4]]
#print(multiplicacionMatrices(A,B))
    
#2. Prueba
suma = opPolinomios()
#Suma de polinomios
listaS = []
for i in range(len(suma)-1,0,-1):
    if suma[i] != 0:
        if suma[i] > 0:
            cad = '+'+str(suma[i])+'X^'+str(i)
            listaS.append(cad)
        else:
            cad = str(suma[i])+'X^'+str(i)
            listaS.append(cad)
print(''.join(str(e) for e in listaS))
#Multiplicacion de polinomios
#FALTA TERMINAR ESTA PARTE

##3. Prueba
#str = 'bobazcbobobegbobghbobobaklbobob'            
#cad = 'bob'
#num = subCadena(str, cad)
#print('El número de veces que ',cad,' aparece es: ',num)
    
##4. Prueba
#dic = repeticionesArchivo()
#palabras = list(dic.keys())
#repeticiones = list(dic.values())
#print('El total de palabras encontradas fue de: ',len(palabras))
#print('Palabra','\t','Repeticiones')
#for i in range(len(palabras)):
#    print(palabras[i],':',repeticiones[i])