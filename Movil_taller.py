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

"""
2. Calcular el número de pulsaciones que una persona debe tener por
cada 10 segundos de ejercicio, si la fórmula es:
Num. Pulsaciones = (200 – edad) /10.
"""
e = int(input('Digite el valor de la edad : '))
pulsaciones = (200 - e)/10
print('El numero de pulsaciones es de :', pulsaciones)

"""
3. Tres personas deciden invertir su dinero para fundar una empresa.
Cada una de ellas invierte una cantidad distinta. Obtener el porcentaje
que cada quien invierte con respecto a la cantidad total invertida.
"""
t1 = float(input("Digite la cantidad que invirtio :"))
t2 = float(input("Digite la cantidad que invirtio :"))
t3 = float(input("Digite la cantidad que invirtio :"))

total = t1+t2+t3
p1 = (t1 / total)*100
p2 = (t2 / total)*100
p3 = (t3 / total)*100

print(f'EL porcentaje del primer inversor es de {p1} %')
print(f'EL porcentaje del primer inversor es de {p2} %')
print(f'EL porcentaje del primer inversor es de {p3} %')

      
 





