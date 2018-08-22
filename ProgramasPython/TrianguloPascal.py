# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""

#def solve(A):
#    A = A - 1
#    linea = [1]
#    for j in range(A):
#        linea.append(int(linea[j]*(A-j)/(j+1)))
#    return linea
#lineaPascal = solve(3)

def trianguloPascal(A):
    triangulo = []
    for i in range(1, A+1):
        i = i - 1
        linea = [1]
        for j in range(i):
            linea.append(int(linea[j]*(i-j)/(j+1)))
#        print(linea)
        triangulo.append(linea)
    return triangulo

pascal = trianguloPascal(5)


