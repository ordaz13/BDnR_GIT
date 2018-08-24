# -*- coding: utf-8 -*-
"""
@author: flopezg
Este programa muestra las instrucciones básicas para apertura, lectura y
escritura de archivos de texto.
"""

# Lee datos desde un archivo, los multiplica por 2 y
# los escribe en otro archivo.
print('Inicié lectura y escritura de archivos')

# Apertura del archivo.
flec= open('Datos.txt','r')         #Con 'r' el arch. se abre para lectura.
fesc= open('Resultados.txt','w')    #Con 'w' se abre para escritura.

#Escritura en el archivo de salida.
fesc.write('Los números, y su multiplicación por 2, son: \n')

# Lectura desde archivo (cada línea se lee como cadena):
for línea in flec:
  arre = línea.split(',')   	# Para separar cada número.

  for num in arre:
    num2= float(num) * 2
    salida= str(num) + '\t' + str(num2) + '\n'
    fesc.write(salida)    #Escritura en el archivo de salida.
      
# Cierra archivos.
flec.close()
fesc.close()
print('Terminé lectura y escritura de archivos')

