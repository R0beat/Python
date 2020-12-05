# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 23:12:49 2020

@author: González
"""
import numpy as np
import scipy as sc
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#Leemos el archivo
compañias = pd.read_csv("./companies79.csv")
'''El método head()se utiliza para devolver las primeras n filas 
(5 por defecto) de un marco de datos o una serie.'''
compañias.head()
#Eliminamos la fila Unamed
compañias.drop("Unnamed: 0",axis=1,inplace=True)
compañias.info()

compañias.head()
'''Guarda en una variable Xf todas las variables sin incluir Compañia
ni Sector.'''
xf = compañias[compañias.columns[1:7]]
xf.head()

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
compañia_escalada = scaler.fit_transform(xf.values)
compañia_estandarizada = pd.DataFrame(compañia_escalada,
                                       columns=xf.columns)
compañia_estandarizada

'''Dibuja un gráfico de boxplot múltiple (matrixplot) donde se
vea un boxplot para cada variable.'''

plt.figure(figsize=(14,8)) #controla el tamaño del gráfico
sns.boxplot(data = compañia_estandarizada)
plt.xticks(rotation=90) #controla la rotación de las etiquetas en el eje X
plt.show()

'''Se observan algunas observaciones que puedan ser datos atípicos o
outliers?'''
compañia=compañia_estandarizada[compañia_estandarizada.apply(lambda x: np.abs(x - x.mean()) / x.std() < 6).all(axis=1)]
compañia.shape

compañia["Id"] = compañia.index
xf["Id"] = xf.index

compañia.info()
xf.info()

plt.figure(figsize=(14,8))
sns.boxplot( data = compañia[compañia.columns[:7]])
plt.xticks(rotation=90)  
plt.show()
''' Ahora dibuja los boxplots para cada variable teniendo en cuenta la
variable Sector para estudiar cada variable según cada sector'''
xf[["Id","V8"]]

compañia_diagnostico = compañia.join(xf[["Id","V8"]].set_index(["Id"]),
                                               on=["Id"],
                                               how="inner")
compañia_diagnostico.head()

compañia_diagnostico.drop("Id",axis=1,inplace = True)
compañia_diagnostico.info()



plt.figure(figsize=(14,8))
compañias_diagnostico.boxplot(by="V8",figsize=(24,12))
plt.xticks(rotation=90)
plt.show()

compañias_diagnostico.shape

from scipy.stats import norm

f, axes = plt.subplots(2, 3, figsize=(10, 10), sharex=True)
sns.distplot(xf["V2"],bins=20,fit=norm, kde=False,color='INDIANRED',ax=axes[0, 0])
sns.distplot(xf["V3"],bins=20,fit=norm, kde=False,color='INDIANRED',ax=axes[0, 1])
sns.distplot(xf["V4"],bins=20,fit=norm, kde=False,color='INDIANRED',ax=axes[0, 2])
sns.distplot(xf["V5"],bins=20,fit=norm, kde=False,color='INDIANRED',ax=axes[1, 0])
sns.distplot(xf["V6"],bins=20,fit=norm, kde=False,color='INDIANRED',ax=axes[1, 1])
sns.distplot(xf["V7"],bins=20,fit=norm, kde=False,color='INDIANRED',ax=axes[1, 2])
plt.show()


