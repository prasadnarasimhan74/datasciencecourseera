# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 10:43:07 2017

@author: User
"""

import numpy as  np
import matplotlib.pyplot as plt
from sklearn import linear_models,datasets

#import data to play with
iris = datasets.load_iris()
X = iris.data[:,:2]
Y = iris.target

h=0.2 # Step size in mesh

logreg = linear_models.LogisticRegression(C=1e5)
logreg.fit(X,Y)

# Plot the decision boundary For that we will assign to color to each
# point in the mesh [x_min,x_max]x[y_min,y_max]

x_min , x_max = X[:,0].min() - .5,X[:,0].max() + .5
y_min, y_max =  X[:,1].min() - .5,X[:,1].max() + .5
xx,yy = np.meshgrid(np.arange(x_min,x_max,h),np.arange(y_min,y_max,h))
z=logreg.predict(np.c_[xx.ravel(),yy.ravel()])

#Put the result into a Color Plot
Z=Z.reshape(xx.shape)
plt.figure(1,figsize(4,3))
plt.pcolormesh(xx,yy,cmap,plt.cm.Paired)

#Plot also the training points
plt.scatter(X[:,0],X[[:,1],c_Y,edgecolors,'k',cmap,plt.cm.Paired])
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')

plt.xlim(xx.min(),xx.max())
plt.ylim(yy.min(),yy.max())

plt.xticks()
plt.yticks()

plt.show()