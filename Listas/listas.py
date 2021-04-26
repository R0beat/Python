# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 05:11:33 2021

@author: González
"""

compras = ['Huevo','Leche','Queso','Jabón']
precio = [15,24,20,10]

print(f'EL {compras[0]} tiene un valor de {precio[0]}')

# Mutabilidad
# Las listas tienen la característica de permitirnos modificar el valor de alguno de sus elementos. 

precio[0]=19

"""
Métodos de las listas
Podemos inicializar una lista de números a través de una función llamada range( a, b, in ):
a es el límite inferior de la secuencia de números
b es el límite superior (éste se excluye).
in es la unidad de incremento (argumento opcional)
"""
aleatorio = range(1,30,2)

lista_aleatorio = list(aleatorio)

lista_aleatorio
# Longitud de la lista
len(lista_aleatorio)

# Para agregar un elemento utilizamos el método append()
lista_aleatorio[:15] + [30]

# Podemos comprobar si algún valor existe dentro de una lista a través del término in
3 in [1, 2, 3]

# También podemos trabajar con listas anidadas, asignando listas como valores en una lista.

fila_1=[1,2,3]
fila_2=[4,5,6]
fila_3=[7,8,9]
matriz=[fila_1,fila_2,fila_3]
matriz