# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 14:37:39 2017

@author: User
"""

import operator
def getNeighbors(trainingSet,testInstance,k):
    distances = []
    length = len(testInstance)-1
    for x in range(len(trainingSet)):
        dist = euclideanDistance(testInstance,trainingSet[x],dist)
        distances.append((trainingSet[x],dist))
        distances.sort(key=operator.itemgetter(1))
        neighbors = []
        for x in range(k):
            neighbors.append(distances[x][0])
        return neighbors
    trainSet[[2,2,2,'a'],[4,4,4,'b']]
    testInstance=[5,5,5]
    k=1
    neighbors = getNeighbors(trainSet,testInstance,1)
    print(neighbors)