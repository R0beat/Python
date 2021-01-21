# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 22:54:05 2020

@author: González
"""
#%%
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('./anova.csv')
#Sumamos el contenido de las columnas X, Y
sum_x = df ['x'].sum()
sum_y = df ['y'].sum()
#Elevamos al cuadrado y creamos 2 columnas
df['x2']=df['x'].apply(lambda x: pow(x,2))
df['y2']=df['y'].apply(lambda x: pow(x,2))
#Sumamos el contenido de las nuevas columnas
sum_x2=df['x2'].sum()
sum_y2=df['y2'].sum()
#Multiplicamos x * y
df['xy'] = df['x']*df['y']
#Sumamos el contenido de xy
sum_xy = df['xy'].sum()
#Ver el numero de elemntos de la columna
n = len(df['x'])
#Obtenemos la media
#Opcion 1
#y_prom=(sum_y/n)
#print(y_prom)
##Opcion2
#print(df['y'].mean())
x_prom = df['x'].mean()
y_prom = df['y'].mean()

print(x_prom)
print(y_prom)
#Obtenemos b1 y b0
b1= (sum_xy-(1/n)*(sum_x*sum_y))/((sum_x2)-(1/n)*pow(sum_x,2))
b0= y_prom-b1*x_prom
print('b1: ',b1)
print('b0: ',b0)

import statsmodels.formula.api as smf
#ols = modelos que ajustaran a este metodo
reg = smf.ols('y~x',data=df)
res= reg.fit()
print('Params: ')
print(res.params)
# Gráfico
# ==============================================================================
lfig, ax = plt.subplots(figsize=(6, 3.84))
ax.plot(b0,b1,marker='o',color='red')

print(df)
#%%

