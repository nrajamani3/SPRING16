# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 08:55:03 2016

@author: nanditharajamani
"""
import numpy
import random
import matplotlib.pyplot as plt
import time
import module3Dmove as 3d


class Virus:
    def __init__(self):
        self.prob = 0
        self.prob4move = 0
        self.prob8move = 0
        self.prob1axis3D = 0
        self.prob2axis3D = 0
        self.prob3axis3D = 0
        self.probnomove3D = 0
        self.x = random.random()
        self.uxx = []
        self.uyy = []
        self.uzz = []
        #self.xcor = []
        #self.ycor = []
        
 
    def move1d(self,np,ns,p0):
         RIGHT = 1; LEFT = 2;
         self.prob      = (1-p0)**2 
         self.prob1 = 1-(self.prob)
         self.uxx = numpy.zeros(np)
         for i in range (np):
            self.uxx[i] = ((np)/2) 
         for step in range (ns): 
            for i in  range (np):
               if (self.x <= self.prob):
                 dir1 = random.choice((1,2))
                 if dir1 == RIGHT:
                   self.uxx[i] += 1
                 elif dir1 == LEFT:
                    self.uxx[i] -= 1
        
         return self.uxx           
         #self.xcor.append(uxx)
         #print("xcor",self.xcor)
    def move2d(self,np,ns,p0):
        #RIGHT = 1; LEFT = 2; UP = 3; DOWN = 4; UP_RIGHT = 5; UP_LEFT = 6;
        #DOWN_RIGHT = 7;DOWN_LEFT = 8
        self.prob4move = 4*(1-(p0))*p0
        self.prob8move = 4*(p0*p0)
        self.uxx = numpy.zeros(np)
        self.uyy = numpy.zeros(np)
        for i in range (np):
            self.uxx[i] = ((np/2))
            self.uyy[i] = ((np/2))
        for  step in range (ns):
            for i in range (np):
                if (self.x <= self.prob4move):
                    self.move_dir2(i)
                elif(self.x <= self.prob4move+self.prob8move):
                    self.move_dir3(i)
         
    def move3d(self,np,ns,p0):
        self.probnomove3D = (1-2*p0)**3
        self.prob1axis3D = 6*(((1-2*p0)**2)*p0)
        self.prob2axis3D = 12*(((1-2*p0)*p0**2))
        self.prob3axis3D = 8*((p0)**3)
        self.uxx = numpy.zeros(np)
        self.uyy = numpy.zeros(np)
        self.uzz = numpy.zeros(np)
        for i in range(np):
            self.uxx[i] = (np/2)
            self.uyy[i] = (np/2)
            self.uzz[i] = (np/2)
        for step in range(ns):
            for i in range(np):
                if(self.x <= self.prob1axis3D):
                   self.move_dir4(i)
                elif(self.x <= self.prob1axis3D+self.prob2axis3D):
                   self.move_dir5(i)
                elif(self.x <= self.prob1axis3D+self.prob2axis3D+self.prob3axis3D):
                   self.move_dir6(i) 

           
    
tstart = time.time()        
s = Virus()
s.move2d(1000,1000,0.2)
tfinish = time.time()
print ("the average time using numpy:", tfinish-tstart, "s")
plt.hist(s.uxx)
plt.show()
plt.scatter(s.uxx,s.uyy)
plt.show()
#plt.scatter(uyy,uzz)
#plt.show()
#plt.scatter(uxx,uzz)
#plt.show()


                    
                    
                    
                 
           
              
         
        