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

"""
4. Un banco da a sus ahorradores un interes de 1.5% sobre el monto
ahorrado. Teniendo como dato de entrada el saldo inicial del
ahorrador determine el saldo final.
"""
s = float(input('Digite el saldo inicial :'))
i = float (s * 0.015)
t = s + i
print(f'El saldo final es de: {t} ')

"""
5. Una empresa le hace los siguientes descuentos sobre el sueldo base
a sus trabajadores: 1% por ley de politica pública, 4% por seguro
social, 0.5% por seguro forzoso y 5% por caja de ahorro. Realice un algoritmo que determine el monto de cada descuento y el monto total
a pagar al trabajador
"""
base = float(input('Digite el salario base : $'))
pp = float (base * 0.01)
ss = float (base * 0.04)
sf = float (base * 0.005)
ca = float (base * 0.05)
 
Total = pp + ss + sf + ca
st=base-Total
print(f'El descuento por politica publica es de : ${pp}')
print(f'El descuento por seguro socail es de : ${ss}')
print(f'El descuento por seguro forzoso es de : ${sf}')
print(f'El descuento por caja de ahorro es de : ${ca}')

print(f'El monto total a pagar es de : ${st}')

"""
6. El periódico el Informador cobra por un aviso clasificado un monto
que depende del número de palabras, tamaño en cetímetros y
número de colores. Cada palabra tiene un costo de $20.000, cada
centímetro tiene un costo de $15.000 y cada color tiene un costo de
$25.000. Realice un algoritmo que determine el monto a pagar por un
aviso clasificado.
"""
np = int(input('Digite el numero de palabras :'))
tc = float(input('Digite el tamaño en centimentro :'))
nc= int(input('Numero de colores :'))
ccp = float (np*20000)
ctc = float (tc*15000)
cnc= float (nc*25000)
suma = ccp + ctc + cnc
print(f' El monto a pagar por un aviso clasificado es de: {suma}')





      
 





