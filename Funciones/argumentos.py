# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 13:59:09 2021

@author: González
"""
# *args es la contracción de argumentos
def argumentos(*args):
    print(args)
# nos devolvera una tupla con los argumentos indeterminados
argumentos(5,'Roberto',[0,1,2,3,4,5])

def argumentos(*args):
    for elemento in args:
        print(elemento)
        
argumentos(5,'Roberto',[0,1,2,3,4,5])
# Podemos renombrar los argumentos
def nombrar(**kwargs):
    print(kwargs)
    
def nombrar(**kwargs):
    for x in kwargs:
        print(x,': ',kwargs[x])
    
nombrar(id=10,nombre='Roberto',notas=[10,10,10])

# Esta función tomara argumentos indeterminados e indeterminados

def super_nominacion(*args, **kwargs):
    # iniciamos el contador suma, sumara los valores numericos args SIN NOMBRE
    suma = 0
    for e in args:
        suma += e

    print('El promedio indeterminado es {}'.format(suma/len(args)))
    # Muestra la clave y el valor asociado a la clave
    for x in kwargs:
        print(x,'\t',kwargs[x])
        
super_nominacion(10,10,20,3,4,id=5,nombre='Roberto Gonzalez',edad=27,notas=[10,10,10,6,6])