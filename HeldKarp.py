# -*- coding: utf-8 -*-
"""
Created on Tue May 18 08:12:45 2021

@author: Albert
"""

from graf import *
import itertools
import time
#sTPS with held-karp algorithm
#Be warned it has to search trough n^2 * 2^n combinations
#n is the number of verticies of the graph

def held_karp(graph,startVertex):
    n = graph.size
    baseList = list(range(n))
    baseList.remove(0)
    costList = []
    for i in baseList:
        costList.append([i,graph.g[i][startVertex]])
    print(len(costList))
    
    for size in range(2,n-1):
        for combi in itertools.combinations(baseList, size):
            for k in baseList:
                currentBestLength = -1
                CurrentBestSequenze = []
                #find min
                for m in combi:
                    print(2)
            print(combi)
            
        

if __name__ == "__main__":
    graph = graphClass()
    graph.generateRand(500,500,4)
    held_karp(graph,0)
    