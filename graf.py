# -*- coding: utf-8 -*-
"""
Created on Tue May 18 08:40:48 2021

@author: Albert
"""

import random
import tkinter as tk

#Distance between two points
def distanceCities(city1,city2):
    return ((city1[0]-city2[0])**2+(city1[1]-city2[1])**2)**0.5
        

class canvasClass():
    def __init__(self,width,height,name):
        self.master = tk.Tk()
        self.master.title(name)
        self.master.geometry(str(width) + 'x' + str(height))
        self.canvas = tk.Canvas(self.master,width = width, height = height)
        self.canvas.pack()
        
        
    def display(self):
        self.master.update_idletasks()
        self.master.update()

#We are going to make this as a complete simple weighted graph to make sure that 
#a hamilton cycle does exsit
class graphClass():
    def __init__(self):
        #List with cities coordinates
        self.cities = []
        #graph
        self.g = []
        #Trail trough
        self.trail = []
        
        self.r = 5 #Radius of the circle drawn
        self.vertexColor = "green"
        
        self.trailColor = "red"
    #Generates size different cities at random coordinates inside of 
    #(0-width,0-height)
    def generateRand(self, width,height,size):
        self.size = size
        for i in range(size):
            self.cities.append([width*random.random(),height*random.random()])
        self.g = []
        for i in range(size):
            tempList = []
            for j in range(size):
                tempList.append(distanceCities(self.cities[i], self.cities[j]))
            self.g.append(tempList)
            
    #Displays the cities
    def displayCities(self,canvas):
        for i in self.cities:
            canvas.canvas.create_oval(i[0]-self.r,i[1]-self.r,i[0]+self.r,i[1]+self.r, fill = self.vertexColor)
        canvas.display()
    #Displays a trail trough the cities
    def displayTrail(self,canvas,t):
        c = t[0]
        for i in t[1:]:
            canvas.canvas.create_line(self.cities[c][0],self.cities[c][1],self.cities[i][0],self.cities[i][1], fill=self.trailColor)
            c = i
        canvas.display()
    def evalTrail(self, t):
        current = t[0]
        distance = 0
        for i in t[1:]:
            distance += self.g[current][i]
            current = i
        return distance
    
if __name__ == "__main__":
    canvas = canvasClass(500,500,"Graf")
    graph = graphClass()
    graph.generateRand(500,500,10)
    graph.displayCities(canvas)
    input("stop ")
    canvas.master.destroy()