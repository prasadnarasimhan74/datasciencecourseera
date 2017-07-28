# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 15:58:37 2017

@author: User
"""

#Scatter Plot Matrix
import matplotlib.pyplot as plt
import pandas
from pandas.plotting import scatter_matrix
url = "https://goo.gl/vhm1eU"
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = pandas.read_csv(url,names=names)
scatter_matrix(data)
plt.show()