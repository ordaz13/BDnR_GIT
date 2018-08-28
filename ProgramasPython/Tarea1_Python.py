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
def lec_convDeArchivo(archivo):
    arch = open(archivo,'r')
    cad = arch.read()
    listaCad = cad.split('\n')
    arch.close()
    pol1 = listaCad[0]; pol1 = pol1.split(' '); pol1 = pol1[0:-2]
    pol1 = list(map(float,pol1))
    coef1 = pol1[0:len(pol1):2]; exp1 = pol1[1:len(pol1):2]
    exp1 = list(map(int,exp1))
    pol2 = listaCad[1]; pol2 = pol2.split(' '); pol2 = pol2[0:-2]
    pol2 = list(map(float,pol2))
    coef2 = pol2[0:len(pol2):2]; exp2 = pol2[1:len(pol2):2]
    exp2 = list(map(int,exp2))
    return coef1, coef2, exp1, exp2

def imprimePolinomio(lista):
    listaS = []
    for i in range(len(lista)-1,0,-1):
        if lista[i] != 0:
            if lista[i] > 0:
                cad = '+'+str("%.1f" %lista[i])+'X^'+str(i)
                listaS.append(cad)
            else:
                cad = str("%.1f" %lista[i])+'X^'+str(i)
                listaS.append(cad)
    cadF = ''.join(str(e) for e in listaS)
    return cadF

def opPolinomios():
    coef1,coef2,exp1,exp2 = lec_convDeArchivo('Polinomios.txt')
    #suma
    sumP1 = [0 for i in range(16)]
    for i in range(len(coef1)):
        sumP1[exp1[i]] = coef1[i]
    sumP2 = [0 for i in range(16)]
    for j in range(len(coef2)):
        sumP2[exp2[j]] = coef2[j]
    suma = [p1+p2 for p1,p2 in zip(sumP1, sumP2)]
    #multiplicacion
    resCoef = [] 
    resExp = []
    for i in range(len(coef1)):
        for j in range(len(coef2)):
            resCoef.append(coef1[i]*coef2[j])
            resExp.append(exp1[i]+exp2[j])
    mult = [0 for i in range(max(resExp)+1)]
    for k in range(len(resCoef)):
        mult[resExp[k]] = mult[resExp[k]] + resCoef[k]
    return suma, mult

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

#5.
def numElemTot(dic):
    lista = list(dic.values())
    suma = 0
    for elem in lista:
        if ((type(elem)==list) or (type(elem)==tuple) or (type(elem)==dict) or (type(elem)==set)):
            suma = suma + len(elem)
        else:
            suma = suma + 1
    return suma

#6.


##1. Prueba
##Lectura de archivo
#arch = open('Matrices.txt','r')
#cad = arch.read()
#listaCad = cad.split('\n')
#c1 = listaCad[0].split(';'); c1 = c1[0:len(c1)-1]
#c2 = listaCad[1].split(';'); c2 = c2[0:len(c2)-1] 
#mat1 = []; mat2 = []
#for i in range(len(c1)):
#    mat1.append(c1[i].split(' '));
#for j in range(len(c2)):
#    mat2.append(c2[j].split(' '));
#for k in range(len(mat1)):
#    mat1[k] = list(map(int,mat1[k]))
#for l in range(len(mat2)):
#    mat2[l] = list(map(int,mat2[l]))
#print(multiplicacionMatrices(mat1,mat2))
##Matrices dadas
#A = [[1,2],[3,4]]
#B = [[1,2],[3,4]]
##Multiplicacion de matrices
#print(multiplicacionMatrices(A,B))

##2. Prueba
#suma, mult = opPolinomios()
##Suma de polinomios
#print(imprimePolinomio(suma))
##Multiplicacion de polinomios
#print(imprimePolinomio(mult))

##3. Prueba
#palabra = 'bobazcbobobegbobghbobobaklbobob'            
#cad = 'bob'
#num = subCadena(palabra, cad)
#print('El número de veces que ',cad,' aparece es: ',num)
    
##4. Prueba
#dic = repeticionesArchivo()
#palabras = list(dic.keys())
#repeticiones = list(dic.values())
#print('El total de palabras encontradas fue de: ',len(palabras))
#print('Palabra','\t','Repeticiones')
#for i in range(len(palabras)):
#    print(palabras[i],':',repeticiones[i])
    
##5. Prueba
#dic = {1:1, 2:6.6, 3:'x', 4:'matenme', 5:['a','b','c'], 6:['odio','vivir'], 
#       7:('no','valgo','la','pena'), 8:{'a':1,'b':2,'c':3}}
#cuentaTot = numElemTot(dic)
#print('El total de elementos en la lista es: ',cuentaTot)
    
#6. Prueba

