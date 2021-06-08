# -*- coding: utf-8 -*-
"""
Created on Wed May 26 23:24:17 2021

@author: Albert
"""

from graf import *
from NearestNeighbour import *
from depthfirst import *
from HeldKarp import *
import time
import matplotlib.pyplot as plt
import tikzplotlib 

nearestNeighbourAcc = []
for i in range(4,11):
    totalAcc = 0
    for j in range(5):
        graf = graphClass()
        graf.generateRand(500,500,i)
        totalAcc += nearestNeighbour(graf,0)[1]/depthFirst(graf,0)[1]
    nearestNeighbourAcc.append(totalAcc/5-1)
print(nearestNeighbourAcc)

plt.figure(1)
plt.ylabel("Antal % støre end mindste")
plt.xlabel("Antal knuder")

plt.plot(list(range(4,11)),nearestNeighbourAcc)
tikzplotlib.save("fejl.tex")
plt.show()
timeNN = []
timeKP = []
timeDP = []
maxN = 11
for i in range(4,maxN):
    totalTime = 0 
    for j in range(5):
        graf = graphClass()
        graf.generateRand(500,500,i)
        timeNow = time.time()
        nearestNeighbour(graf,0)
        totalTime += (time.time() - timeNow)
    timeNN.append(totalTime/5)
    
    totalTime = 0
    for j in range(5):
        graf = graphClass()
        graf.generateRand(500,500,i)
        timeNow = time.time()
        held_karp(graf,0)
        totalTime += (time.time() - timeNow)
    timeKP.append(totalTime/5)
    
    totalTime = 0
    for j in range(5):
        graf = graphClass()
        graf.generateRand(500,500,i)
        timeNow = time.time()
        depthFirst(graf,0)
        totalTime += (time.time() - timeNow)
    timeDP.append(totalTime/5)
plt.figure(2)
liste = list(range(4,maxN))
print(timeNN)
print(timeKP)
print(timeDP)
plt.ylabel("Tid for at finde minimum hamilton-cyklus")
plt.xlabel("Antal knuder")
plt.plot(liste,timeNN,"b")
plt.plot(liste,timeKP,"g")
plt.plot(liste,timeDP,"r")
tikzplotlib.save("tid.tex")
plt.show()