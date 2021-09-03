# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 09:15:18 2021

@author: Usuario
"""
"""
1. Haga un algoritmo que calcule la masa de la siguiente fórmula:
Masa = (presión * volúmen) / (0.37 * (temperatura + 460))
"""
p = float(input('Digite el valor de la presion : '))
v = float(input('Digite el valor del volumen :'))
t = float(input('Digite el valor de la temperatura : '))
masa = (p*v)/(0.37*(t+460))
print('El valor de la masa es de : ' , masa)


