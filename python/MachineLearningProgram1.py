# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 15:08:29 2017

@author: User
"""

from sklearn.preprocessing import StandardScaler
import pandas
import numpy
url = "https://goo.gl/vhm1eU"
names = ['preg','plas','pres','skin','test','mass','pedi','age','class']
data_frame = pandas.read_csv(url,names=names)
array=data_frame.values
#Separate Arrayinto input and output components
X = array[:,0:8]
Y = array[:,8]
scaler = StandardScaler().fit(X)
rescaledX = scaler.transform(X)
# summarise transformed data
numpy.set_printoptions(precision=3)
print(rescaledX[0:5,:])