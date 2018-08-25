# -*- coding: utf-8 -*-

# Lee datos desde teclado, los guarda en un arreglo, los
# multiplica por 2 y los escribe en pantalla.

# Con estas dos instrucciones se lee desde teclado:

cad= input('Escribe numeros separados por comas:')
arre = cad.split(',')

print('Los numeros del arreglo multiplicados por 2 son:')
for num in arre:
  print(int(num) * 2)

