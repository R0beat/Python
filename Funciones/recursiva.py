# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 14:47:58 2021

@author: González
"""

#%% FUNCIONES RECURSIVAS
# una función recursiva se utiliza a si misma en el mismo cuerpo de su definición
def cuenta_atras(num):
    # contador en regresión de 1 en 1
    num -= 1
    # Si el contador es mayor a 0 ejecuta de nuevo la función
    if num > 0:
        print(num)
        cuenta_atras(num)
    # Cuando es igual a 0 ya no ejecuta la funcióny se pasa al else 
    else:
        print(num,'boom \a')
        print('Fin de la función ', num)
    
cuenta_atras(5)
#%% Factorial
def factorial(num):
    # Toma el valor inicila
    print('Valor inicial ',num)
    # Si el valor es mayor que 1 asigna a num lo multiplica por la función restando 1
    if num > 1:
        num = num * factorial(num-1)
        print('Factorial ',num)
    return num
factorial(5)

