# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 13:18:35 2018

@author: super
"""

#Escribe datos a un archivo csv
import csv
with open('eggs.csv', 'w') as csvfile:
    spamwriter = csv.writer(csvfile) 
    spamwriter.writerow(['Hola', 1, 2, 3])
    spamwriter.writerow(['Adiós', 3, 2, 1])
csvfile.close()
