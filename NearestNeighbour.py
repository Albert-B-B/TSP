# -*- coding: utf-8 -*-
"""
Created on Tue May 18 09:59:53 2021

@author: Albert
"""

from graf import *

#Implementation of the nearest neighbour approch
def nearestNeighbour(graph,startVertex):
    trail = [startVertex]
    current = startVertex
    totalDistance = 0
    bestVertex = -1
    for j in range(len(graph.g)-1):
        best = -1
        for i in range(len(graph.g)):
            notVisited = True
            if i in trail:
                notVisited = False
            if notVisited:
                if best == -1:
                    best = graph.g[current][i]
                    bestVertex = i
                elif graph.g[current][i] < best and graph.g[current][i] != 0:
                    best = graph.g[current][i]
                    bestVertex = i
        current = bestVertex
        trail.append(bestVertex)
        totalDistance += best
    trail.append(startVertex)
    totalDistance += graph.g[current][startVertex]
    return (trail,totalDistance)
        
    
if __name__ == "__main__":
    canvas = canvasClass(500,500,"Graf")
    graph = graphClass()
    graph.generateRand(500,500,1000)
    graph.displayCities(canvas)

    trail, length = nearestNeighbour(graph, 0)
    #print(trail)
    print(length)
    graph.displayTrail(canvas,trail)
    canvas.master.mainloop()
    #canvas.master.destroy()