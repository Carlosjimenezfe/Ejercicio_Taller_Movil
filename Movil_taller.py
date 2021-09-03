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

"""
7. Una empresa paga a sus empleados un bono por antigüedad que
consiste en $100.000 por el primer año laboral y $120.000 por cada
año siguiente. Realice un algoritmo que determine el monto del bono
a pagar a un trabajador que tiene varios años en la empresa.
"""
nn = int(input('Digite el numero de años laborando :'))
total = nn*120000
print(f'El monto del bono a pasar del trabajador es de : ${total}')

"""
8. Una Universidad le paga a sus profesores $20.000 la hora y le hace
un descuento del 5% por concepto de caja de ahorro. Determine el
monto del descuento y el monto total a pagar al profesor.
"""

nh = int(input("Digite la cantidad de horas :"))
pnh = nh*20000
d = pnh*0.05
total = pnh-d
print(f'El descuento es de : ${d}')
print(f'El total a pagar es de : ${total}')

"""
9. Un centro de comunicaciones alquilan tarjetas para realizar llamadas
y cobran el monto consumido de la tarjeta mas un recargo del 20%.
Teniendo como dato de entrada el monto inicial y el monto final de la
tarjeta, determine el costo de la llamada
"""
mi = float (input('Digite el monto inicial : $'))
mf = float (input('Digite el monto final : $'))
cll=(mi-mf)/0.20
print(f'El monto a pagar es de : ${cll}')

"""
En una fototienda cobran por el revelado de un rollo $1.500 por cada
foto. Realice un algoritmo que determine el monto a pagar por un
revelado completo sabiendo que adiconalmente le cobran el IVA
(16%).      
"""
nf=int(input('Digite el numero de fotos :')) 
ccf = nf*1500
ti = ccf*0.16
total = ccf + ti
print(f'El monto a pagar es de : ${total}')


"""
En un hospital existen tres áreas: Ginecología, Pediatría y
Traumatología. El presupuesto anual del hospital se reparte
conforme a la siguiente tabla:
"""
pa = float (input('Digite el presupuesto anual : $'))
g = pa*0.40
t = pa*0.30
p = pa*30
print(f'La cantidad de dinero que recibe el area de gincelogia es de : ${g}')
print(f'La cantidad de dinero que recibe el area de traumatologia es de : ${t}')
print(f'La cantidad de dinero que recibe el area de pediatria es de : ${p}')

"""
 Una video tienda alquila DVD a $1.500 el día. Tiene una promoción
que consiste en dejar gratis el alquiler de una película. Realice un
algoritmo que teniendo como dato de entrada el total de películas
alquiladas, y el número de días de alquiler, determine el monto a
pagar
"""
np = int(input('Digite el numero de peliculas :'))
nd = int(input('Digite el numero de dias :'))
total = np*nd*1500
print(f'El monto a pagar es de :${total}')

"""
Una Agencia de viajes cobra por un Tour a Cartagena $25.000
diarios por persona. Realice un algoritmo que determine el monto a
pagar por una familia que desee realizar dicho Tour sabiendo que
también cobran el 12% de IVA.
"""
np = int(input('Digite el numero de personas : '))
tnp = np*25000
iva = tnp*0.12
total = tnp+iva
print(f'El monto a pagar es de : ${total}')

"""
Un Hotel 5 Estrellas de Santa Marta tiene una promoción para sus
clientes. Cobra por una habitación $100.000 el primer día y por el
resto $200.000 por día. Realice un algoritmo que determine el valor
total a pagar por la habitación si la estadía fue de varios días.
"""

nd = int(input('Digite el numero de dias : '))
total=nd*200000-100000
print(f'El total a pagar es de : ${total}')

"""
El banco del Pueblo da microcréditos a empresarios para ser
cancelados en un lapso de 2 años (24 meses). Al monto del
préstamo se le cobra un interés del 24%. El empresario debe pagar
la mitad del préstamo en 4 cuotas especiales y la otra mitad en 20
cuotas ordinarias. Realice un algoritmo que teniendo como dato de
entrada el monto del préstamo, determine el monto total a pagar por
el préstamo, el monto de las cuotas especiales y el monto de las
cuotas ordinarias
"""
monto = float (input('Digite el monto a prestar $'))
interes = monto*0.24
ta = monto+interes
mce = ((ta/2)/4)
mco = ((ta/2)/20)
print(f'El monto total a pagar es de : ${ta}')
print(f'El monto de las cuotas especiales : ${mce}')
print(f'El monto de las cuotas especiales : ${mco}')
