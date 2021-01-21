# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.


"""

import pandas as pd

df=pd.read_csv('./cars.csv')

#%%
#Importamos el modelo statsmodels.formula.api y la renombram 'smf'  
import statsmodels.formula.api as smf
#ols = Ordninary Least Squares    
'''En estadística, los mínimos cuadrados ordinarios o mínimos cuadrados 
lineales es el nombre de un método para encontrar los parámetros 
poblacionales en un modelo de regresión lineal. Este método minimiza la 
suma de las distancias verticales entre las respuestas observadas en 
la muestra y las respuestas del modelo'''
#Escribimos la parte del módelo
''' la columna de consumo dependera de la suma de 
cilindraje + potencia + peso'''
reg = smf.ols('consumo ~ cilindraje + potencia + peso', data = df)
#fit()
'''To elaborate: Fitting your model to (i.e. using the .fit() method on)
 the training data is essentially the training part of the modeling process. 
 It finds the coefficients for the equation specified via the algorithm 
 being used (take for example umutto's linear regression example, above).

Then, for a classifier, you can classify incoming data points 
(from a test set, or otherwise) using the predict method. Or, in the 
case of regression, your model will interpolate/extrapolate when predict 
is used on incoming data points.

It also should be noted that sometimes the "fit" nomenclature is used 
for non-machine-learning methods, such as scalers and other preprocessing 
steps. In this case, you are merely "applying" the specified function to 
your data, as in the case with a min-max scaler, 
TF-IDF, or other transformation.'''
res= reg.fit()
print(res.summary())
print('R-squared: ', res.rsquared)

#%%