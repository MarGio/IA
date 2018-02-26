# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 19:14:55 2018

@author: mario
"""

def operacionOR(x,y):
    if((-10 + 20*x + 20*y)>0):
        return 1
    else:
        return 0
print(operacionOR(0,0))
print(operacionOR(0,1))
print(operacionOR(1,0))
print(operacionOR(1,1))