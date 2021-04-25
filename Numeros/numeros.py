# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 13:21:10 2021

@author: González
"""
#%% Enteros
x = 300
print(x)
x.__add__(50)

x2=x.__add__(50)
x2

print(x2 + x)

#%% Flotantes
y = 4.5
print(y)

type(y)

#%% Complejos Para números complejos, o sea, de la forma (A + Bj) donde la unidad imaginaria está representada por j.
z = 1 + 2j
z,type(z)

parte_real=z.real
parte_imag=z.imag
print(parte_real," ",parte_imag)
