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
    bestLength = graph.evalTrail((startVertex,) + bestTrail + (startVertex,))
    for i in combinations:
        if graph.evalTrail((startVertex,) + i + (startVertex,)) < bestLength:
            bestLength = graph.evalTrail((startVertex,) + i + (startVertex,))
            bestTrail = i
    return ((startVertex,)+bestTrail+(startVertex,),bestLength)
if __name__ == "__main__":
    #canvas = canvasClass(500,500,"Graf")
    lastTime = time.time()
    i = 1
    graph = graphClass()
    graph.g = [
        [0,2,12,11],
        [2,0,6,4],
        [12,6,0,8],
        [11,4,8,0]
        ]
    graph.size = 4
    print(depthFirst(graph,0))
    while  i <= 10:
        break
        i += 1
        graf = graphClass()
        graf.generateRand(500,500,i)
        lastTime = time.time()
        print(i)
        print(depthFirst(graf,0))
        print(time.time()-lastTime)
        print()
        
