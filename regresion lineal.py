# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 20:35:31 2018

@author: mario
"""

Metros = [5, 15, 20, 25]
Precios = [375, 487, 450, 500]
listaM = (len(Metros))
listaP = (len(Precios))
contador = 0
XiTi = 0
Xi = 0
Ti = 0
Ti2 = 0
Ti22 = 0
while contador<=(listaM-1):
    XiTi += Metros[contador]*Precios[contador]
    Xi += Precios[contador]
    Ti += Metros[contador]
    Ti2 += Metros[contador]**2
    contador = contador + 1

Ti22 = Ti**2
p = (((listaM*XiTi)-(Xi*Ti))/((listaM*Ti2)-Ti22))   
a = ((Xi/listaM)-(p*(Ti/listaP)))
Xt = a+(p*35)
print("xiti:", XiTi)
print("xi:", Xi)
print("ti:", Ti)
print("ti2:", Ti2)
print("ti22:", Ti22)
print("Pendiente b=",p)
print("Interseccion a=",a)
print("Pronostico Xt=",Xt)