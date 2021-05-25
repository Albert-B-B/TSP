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
    cost = {}
    for i in baseList:
        cost[1<<i] = [graph.g[i][0],0]
    print(cost)
    print("")

    for size in range(2,n):
        for combi in itertools.combinations(baseList, size):
            baseLastId = 0
            for j in combi:
                baseLastId += (1<<j)
            cost[baseLastId] = []
            for k in combi:
                lastId = baseLastId - (1<<k)
                
                bestLength = -1
                bestNode = 0
                #find min
                for p in combi:
                    if p == k or p == 0:
                        continue
                    mystery = 2*(p - bin(lastId)[2:2+p].count("0")-1)
                    
                        
                     
                    if cost[lastId][mystery] + graph.g[k][p] == 675.2522835596925:
                        count = 0
                        print(bin(lastId)[:1:-1])
                        for i in range(len(bin(lastId)[:1:-1])):
                            if (bin(lastId)[:1:-1])[i] == "1":
                                count += 1
                            print("test",i,bin(lastId)[2+i],count)
                            if count == p:
                                count = i
                                break
                        
                        print("m",mystery,"p",p,"k", k, "lastId", lastId, "combi", combi, "count", count)
                    
                    if bestLength == -1:
                        bestLength = cost[lastId][mystery] + graph.g[k][p]
                        bestNode = p
                        
                    if bestLength >= cost[lastId][mystery] + graph.g[k][p]:
                        bestLength = cost[lastId][mystery] + graph.g[k][p]
                        bestNode = p
                cost[baseLastId].append(bestLength)
                cost[baseLastId].append(bestNode)

            
    largestId = 0

    
    for i in baseList:  
        largestId += 1<<i
    smallest = float_info.max

    for i in baseList:
        print(cost[largestId][2*(i-1)]+graph.g[i][0])
        if smallest >= cost[largestId][2*(i-1)]+graph.g[i][0]:
            smallest = cost[largestId][2*(i-1)]+graph.g[i][0]
            smallestNode = i
    
    trail = [0]
    
    print("")
    print(cost)
    print("")
    for i in range(n-1):
        trail.append(smallestNode)
        newLargestId = largestId - (1 << smallestNode)
        count = 0
        for i in range(len(bin(largestId)[2:])):
            if bin(largestId)[2+i] == "1":
                count += 1

            if 1 << (i+1) == 1 << smallestNode:
                break
        
        smallestNode = cost[largestId][2*(count-1)+1]
        largestId = newLargestId

    trail.append(0)
    trail.reverse()
    return (trail,smallest)

def held_karp_pro(dists):
    """
    Implementation of Held-Karp, an algorithm that solves the Traveling
    Salesman Problem using dynamic programming with memoization.
    Parameters:
        dists: distance matrix
    Returns:
        A tuple, (cost, path).
    """
    n = len(dists)

    # Maps each subset of the nodes to the cost to reach that subset, as well
    # as what node it passed before reaching this subset.
    # Node subsets are represented as set bits.
    C = {}

    # Set transition cost from initial state
    for k in range(1, n):
        C[(1 << k, k)] = (dists[0][k], 0)

    # Iterate subsets of increasing length and store intermediate results
    # in classic dynamic programming manner
    for subset_size in range(2, n):
        for subset in itertools.combinations(range(1, n), subset_size):
            # Set bits for all nodes in this subset
            bits = 0
            for bit in subset:
                bits |= 1 << bit

            # Find the lowest cost to get to this subset
            for k in subset:
                prev = bits & ~(1 << k)

                res = []
                for m in subset:
                    if m == 0 or m == k:
                        continue
                    res.append((C[(prev, m)][0] + dists[m][k], m))
                C[(bits, k)] = min(res)

    # We're interested in all bits but the least significant (the start state)
    bits = (2**n - 1) - 1

    # Calculate optimal cost
    res = []
    for k in range(1, n):
        res.append((C[(bits, k)][0] + dists[k][0], k))
    opt, parent = min(res)

    # Backtrack to find full path
    path = []
    for i in range(n - 1):
        path.append(parent)
        new_bits = bits & ~(1 << parent)
        _, parent = C[(bits, parent)]
        bits = new_bits

    # Add implicit start state
    path.append(0)

    return opt, list(reversed(path))
    """
    Implementation of Held-Karp, an algorithm that solves the Traveling
    Salesman Problem using dynamic programming with memoization.
    Parameters:
        dists: distance matrix
    Returns:
        A tuple, (cost, path).
    """
    n = len(dists)

    # Maps each subset of the nodes to the cost to reach that subset, as well
    # as what node it passed before reaching this subset.
    # Node subsets are represented as set bits.
    C = {}

    # Set transition cost from initial state
    for k in range(1, n):
        C[(1 << k, k)] = (dists[0][k], 0)

    # Iterate subsets of increasing length and store intermediate results
    # in classic dynamic programming manner
    for subset_size in range(2, n):
        for subset in itertools.combinations(range(1, n), subset_size):
            # Set bits for all nodes in this subset
            bits = 0
            for bit in subset:
                bits |= 1 << bit

            # Find the lowest cost to get to this subset
            for k in subset:
                prev = bits & ~(1 << k)

                res = []
                for m in subset:
                    if m == 0 or m == k:
                        continue
                    res.append((C[(prev, m)][0] + dists[m][k], m))
                C[(bits, k)] = min(res)

    # We're interested in all bits but the least significant (the start state)
    bits = (2**n - 1) - 1

    # Calculate optimal cost
    res = []
    for k in range(1, n):
        res.append((C[(bits, k)][0] + dists[k][0], k))
    opt, parent = min(res)

    # Backtrack to find full path
    path = []
    for i in range(n - 1):
        path.append(parent)
        new_bits = bits & ~(1 << parent)
        _, parent = C[(bits, parent)]
        bits = new_bits

    # Add implicit start state
    path.append(0)

    return opt, list(reversed(path))

if __name__ == "__main__":
    graph = graphClass()
    graph.generateRand(500,500,4)
    graph.g = [
        [0.0, 323.71805560485944, 121.67041377433469, 424.0158714215444], 
        [323.71805560485944, 0.0, 241.59028033162573, 375.6839275617512], 
        [121.67041377433469, 241.59028033162573, 0.0, 311.9915894537321],
        [424.0158714215444, 375.6839275617512, 311.9915894537321, 0.0]]
    
    print(held_karp(graph,0))
    print(depthFirst(graph,0))
    print(held_karp_pro(graph.g))
    # if held_karp(graph,0)[1] != depthFirst(graph,0)[1]:
    #     print(graph.g)
    