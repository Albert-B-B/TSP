# -*- coding: utf-8 -*-
"""
Created on Tue May 18 12:38:44 2021

@author: Albert
"""

from graf import *
import itertools
import time
#sTPS with breadth first search algorithm
#Be warned it has to search trough n! combinations
#n is the number of verticies of the graph

def depthFirst(graph,startVertex):
    n = graph.size
    baseList = list(range(n))
    baseList.remove(startVertex)
    combinations = itertools.permutations(baseList)
    bestTrail = next(combinations)
    bestLength = graph.evalTrail(bestTrail)
    for i in combinations:
        i = (startVertex,) + i + (startVertex,)
        if graph.evalTrail(i) < bestLength:
            bestLength = graph.evalTrail(i)
            bestTrail = i
    return (bestTrail,bestLength)
if __name__ == "__main__":
    #canvas = canvasClass(500,500,"Graf")
    lastTime = time.time()
    i = 1
    while  i <= 10:
        i += 1
        graf = graphClass()
        graf.generateRand(500,500,i)
        lastTime = time.time()
        print(i)
        print(depthFirst(graf,0))
        print(time.time()-lastTime)
        print()
        
