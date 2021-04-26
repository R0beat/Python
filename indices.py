# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 04:25:52 2021

@author: González
"""
"""
Los índices son números ordenados a las variables que nos permiten identificar
valores por su posición
"""

cadena = 'ESTA-CADENA'

# El primer elemento siempre es 0 es el comienzo de la numeración

print(cadena[0],cadena[1],cadena[2],cadena[3])

# Para cada elemento existe un número inverso, de el ultimo al primero empezando con -1
"""
-6 \ -5 \ -4 \ -3 \ -2 \ -1
 C    A    D    E    N    A
 5 /  6 /  7 /  8 /  9 /  10
"""
print(cadena[-6],cadena[-5],cadena[-4],cadena[-3],cadena[-2],cadena[-1])
print(cadena[5],cadena[6],cadena[7],cadena[8],cadena[9],cadena[10])

"""
Slicing

Gracias a los índices podemos seleccionar una secuencia de elementos de una variable. 
Esto se conoce como slicing

La secuencia de elementos la definimos con el formato _[ a : b ]_ . Esto es un rango 
de valores, y el slicing va a devolvernos desde el elemento _a_ hasta el elemento previo al _b_, así que vamos a decir que b está excluido del rango.

TIP : Cuando un rango de valores excluye alguno de sus límites (Siendo _a_ el límite 
inferior, y _b_ el límite superior), se dice que el rango es abierto: 
Abierto por la derecha_ , si excluye a _b_ \
Abierto por la izquierda_ , si excluye a _a_
"""
print(cadena[-6:])
print(cadena[0:4])

