# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 07:46:21 2021

@author: Roberto González
"""

"""
Python es un lenguaje de de típado dinámico y no necesita que se le declaren el
tipo de una variable.

En Python los tipos primitivos son: números, strings, booleanos, listas, tuplas
y diccionarios
"""

#%% Variales enteras
x=10
print(x,type(x))
#%% variables tipo string
nombre = "Conceptos Básicos de Programación"
print(nombre,type(nombre))
#%% Métodos
"""
Son funciones de clase, cada tipo de variable incluye funciones asociadas a ella
"""
x.__add__(10)
# Se pueden saber los métodos disponibles de una varable con la función  dir()
dir(x)

#La función help() nos muestra información más completa de cada variable
help(x)

#%% Diccionarios
diccionario = {'1':x,'2':x.__add__(30)}
print(diccionario)

print(f"{nombre.title()} cuesta ${diccionario['2']}.00 con un descuento de ${diccionario['1']}.00 ")


