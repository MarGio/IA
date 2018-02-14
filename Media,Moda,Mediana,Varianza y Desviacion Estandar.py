# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""
import math
listaMedia = [1525, 257, 378, 9543, 7854, 152]
listaTamaño = (len(listaMedia))
contador = 0
media = 0
while contador<=(listaTamaño-1):
    media += listaMedia[contador]
    contador = contador + 1
    
print("La media es:",(media/listaTamaño))
#*-*- Calcular Media -*-*-*-*-*-*
listaMediana = [1, 1, 2, 2, 3, 3, 4, 5, 6, 7, 9, 9, 9]
listaTamañoMediana = (len(listaMediana))
listaPosicion = listaTamañoMediana/2
mediana = 0
if listaTamañoMediana%2==0:
    mediana=listaMediana[int(listaPosicion)]
    listaPosicion = listaPosicion + 1
    mediana= mediana + listaMediana[int(listaPosicion)]
    print("La mediana es:",(mediana/2))
else:
    mediana=listaMediana[int(listaPosicion)]
    print("La mediana es:",mediana)
 #*-*- Calcular Moda -*-*-*-*-*-*   
listaModa = [1, 1, 2, 2, 3, 3, 4, 5, 6, 7, 9, 9, 9]
repeticiones = 0                                                                         
for i in listaModa:                                                                              
    apariciones = listaModa.count(i)                                                             
    if apariciones > repeticiones:                                                       
        repeticiones = apariciones                                                       
                                                                                         
modas = []                                                                               
for i in listaModa:                                                                              
    apariciones = listaModa.count(i)                                                             
    if apariciones == repeticiones and i not in modas:                                   
        modas.append(i)                                                                  
                                                                                         
print ("La Moda es:", modas)

#*-*- Calcular Varianza y desviacion estandar -*-*-*-*-*-*
listaMediana = [13, 14, 15, 15, 15, 16, 17, 18, 20]
listaTamañoMediana = (len(listaMediana))
listaPosicion = listaTamañoMediana/2
mediana = 0
if listaTamañoMediana%2==0:
    mediana=listaMediana[int(listaPosicion)]
    listaPosicion = listaPosicion + 1
    mediana= mediana + listaMediana[int(listaPosicion)]
else:
    mediana=listaMediana[int(listaPosicion)]
contadorVarianza = 0
varianza = 0
while contadorVarianza<=(listaTamañoMediana-1):
    varianza += (listaMediana[contadorVarianza]-mediana)**2
    contadorVarianza = contadorVarianza + 1

varianza = varianza/listaTamañoMediana
print("La varianza es:",varianza)
desviacionEstandar=math.sqrt(varianza)
print("La desviacion estandar es:",desviacionEstandar)


