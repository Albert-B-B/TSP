# -*- coding: utf-8 -*-
"""
Created on Tue May 18 08:12:45 2021

@author: Albert
"""

from graf import *
from depthfirst import * 
import itertools

from sys import float_info
#sTPS with held-karp algorithm
#Be warned it has to search trough n^2 * 2^n combinations
#n is the number of verticies of the graph

def held_karp(graph,startVertex):
    n = graph.size
    baseList = list(range(n))
    baseList.remove(0)
    
    
    
    
        
    #Structure for saving cases
    cost = {}
    prev = {}
    ends = {}
    #From start to first edges
    for i in baseList:
        cost[1<<i] = [graph.g[i][0]]
        prev[1<<i] = [0]
        ends[1<<i] = [i]
    #How many nodes in sets
    for size in range(2,n):
        #All posible sets
        for combi in itertools.combinations(baseList, size):
            #Id for this combination
            idCombi = 0
            for i in combi:
                idCombi += (1<<i)
            
            cost[idCombi] = []
            prev[idCombi] = []
            ends[idCombi] = []
            #What the end node in the set should be
            for end in combi:
                bestLength = -1
                bestNode = 0
                lastId = idCombi - (1<<end)
                #Loop for finding min cost of getting to that node
                for lastEnd in combi:
                    if end == lastEnd:
                        continue
                    #This line is for finding what the cost for the combination of i that end at lastEnd. 
                    #Just accept this magic and move on
                    getIndex = (bin(lastId)[2:][::-1][:lastEnd]).count("1")
                    if bestLength == -1:
                        bestLength = cost[lastId][getIndex]+graph.g[lastEnd][end]
                        bestNode = lastEnd
                    elif bestLength >= cost[lastId][getIndex]+graph.g[lastEnd][end]:
                        bestLength = cost[lastId][getIndex]+graph.g[lastEnd][end]
                        bestNode = lastEnd
                cost[idCombi].append(bestLength)
                prev[idCombi].append(bestNode)
                ends[idCombi].append(end)
    #For debugging
    # for i in cost:
    #     print(i,cost[i])
    #     print(i,prev[i])
    
    #Finds min cost        
    currId = 0
    for i in baseList:  
        currId += 1<<i    
        
    smallest = cost[currId][0]+graph.g[1][0]
    smallestNode = 0

    for i in baseList[1:]:
        if smallest >= cost[currId][i-1]+graph.g[i][0]:
            smallest = cost[currId][i-1]+graph.g[i][0]
            smallestNode = i

    #Retraces cycle
    cycle = [0]
    for i in range(n-1):
        cycle.append(smallestNode)
        getIndex = (bin(currId)[2:][::-1][:smallestNode]).count("1")

        newNode = prev[currId][getIndex]
        currId -= (1<<smallestNode)
        smallestNode = newNode

    return (cycle, smallest)
    #Return cycle and its length
if __name__ == "__main__":
    graph = graphClass()
    for i in range(0,100):
        graph.generateRand(500,500,7)
        if held_karp(graph,0)[1] != depthFirst(graph,0)[1]:
            print("Error")

    # if held_karp(graph,0)[1] != depthFirst(graph,0)[1]:
    #     print(graph.g)
    