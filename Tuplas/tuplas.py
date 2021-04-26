# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 05:30:36 2021

@author: González
"""
# Tuplas
"""
Una tupla es una secuencia de valores (muy parecida a una lista). Los valores almacenados en una tupla pueden ser de cualquier tipo, y también están indexados.
Se diferencia de las listas en que:
No podemos modificar sus valores luego de crearla (Es inmutable).
Definimos sus valores entre paréntesis, en vez de corchetes.
"""
tupla = ('Lunes','Martes','Miércoles')
tupla

tupla_multi = ([1,2,3],'a',71.4, tupla)
tupla_multi

# Métodos
tupla.index('Lunes') 

tupla_multi.count(71.4)