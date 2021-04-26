# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 13:39:45 2021

@author: González
"""

"""
Funciones se definen con la palabra reservada 'def' las funciones puden recibir
o no recibir parametros así mismo también pude retornar o no un valor
"""

def saludar():
    print('Este es un saludo desde una función')
    
saludar()


def tabla(n):
    for i in range(1,11):
        print(f'{n} * {i} = {n*i}')
        

n = input('Ingresa el numero de la tabla deseada : ')
tabla(int(n))

# Retorno de valores

def funcion():
    return 'Mensaje retonado desde la funcion'

funcion()

def lista():
    return [1,2,3,4,5]

lista()



    
    