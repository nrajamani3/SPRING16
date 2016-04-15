# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 17:25:56 2016

@author: nanditharajamani
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 08:55:03 2016

@author: nanditharajamani
"""
import numpy
import random
import matplotlib.pyplot as plt
import time
#from matplotlib import animation


class Particle:
    def __init__(self):
        self.prob = 0
        self.type = 'x'
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
        self.preX = []
        self.preY =[]
        self.preZ =[]
    def settype(self,t):
        self.type=t
    def nomove(self,np):
        self.uxx = numpy.zeros(np)
        self.uyy = numpy.zeros(np)
        self.uzz = numpy.zeros(np)
        for i in range(np):
            if (self.type == 'v'):
                self.uxx[i] = np/2
                self.uyy[i] = np/2
                self.uzz[i] = (np/2)
            elif (self.type == 'b'):
                self.uxx[i] = i
                self.uyy[i] = 0
                self.uzz[i] = 0
            
    def move_dir2(self,i):
        dir2 = random.choice((1,2,3,4))
        if (dir2 == 1):
            self.uxx[i] += 1
        elif (dir2 == 2):
            self.uxx[i] -= 1
        elif (dir2 == 3):
            self.uyy[i] += 1
        elif(dir2 == 4):
            self.uyy[i] -= 1
    def move_dir3(self,i):
        dir3 = random.choice((5,6,7,8))
        if (dir3 == 5):
            self.uxx[i] += 1
            self.uyy[i] += 1
        elif(dir3 == 6):
            self.uxx[i] -= 1
            self.uyy[i] += 1
        elif(dir3 == 7):
            self.uxx[i] += 1
            self.uyy[i] -= 1
        elif(dir3 == 8):
            self.uxx[i] -= 1
            self.uyy[i] -= 1
    def move_dir4(self,i):
        dir4 = random.choice((1,2,3,4,5,6))
        if dir4 == 1:
          self.uxx[i] += 1
        elif dir4 == 2:
          self.uxx[i] -= 1
        elif dir4 == 3:
          self.uyy[i] += 1
        elif dir4 == 4:
          self.uyy[i] -= 1
        elif dir4 == 5:
           self.uzz[i] += 1
        elif dir4 == 6:
           self.uzz[i] -= 1
    def move_dir5(self,i):
        dir5 = random.choice((7,8,9,10,11,12,13,14,15,16,17,18))
        if dir5 == 7:
           self.uxx[i] += 1
           self.uyy[i] += 1
        elif dir5 == 8:
           self.uxx[i] -= 1
           self.uyy[i] += 1
        elif dir5 == 9:
           self.uxx[i] -= 1
           self.uyy[i] -= 1
        elif dir5 == 10:
           self.uxx[i] += 1
           self.uyy[i] -= 1
        elif dir5 == 11:
           self.uxx[i] += 1
           self.uzz[i] += 1
        elif dir5 == 12:
           self.uxx[i] -= 1
           self.uzz[i] -= 1
        elif dir5 == 13:
           self.uxx[i] += 1
           self.uzz[i] -= 1
        elif dir5 == 14:
           self.uxx[i] -= 1
           self.uzz[i] += 1
        elif dir5 == 15:
           self.uyy[i] += 1
           self.uzz[i] += 1
        elif dir5 == 16:
           self.uyy[i] -= 1
           self.uzz[i] -= 1
        elif dir5 == 17:
           self.uyy[i] += 1
           self.uzz[i] -= 1
        elif dir5 == 18:
           self.uyy[i] -= 1
           self.uzz[i] += 1
    def move_dir6(self,i):
        dir6 = random.choice((19,20,21,22,23,24,25,26))
        if dir6 == 19:
           self.uxx[i] += 1
           self.uyy[i] += 1
           self.uzz[i] += 1
        elif dir6 == 20:
           self.uxx[i] -= 1
           self.uyy[i] -= 1
           self.uzz[i] -= 1
        elif dir6 == 21:
           self.uxx[i] += 1
           self.uyy[i] += 1
           self.uzz[i] -= 1
        elif dir6 == 22:
           self.uxx[i] -= 1
           self.uyy[i] -= 1
           self.uzz[i] += 1
        elif dir6 == 23:
           self.uxx[i] += 1
           self.uyy[i] -= 1
           self.uzz[i] += 1
        elif dir6 == 24:
           self.uxx[i] -= 1
           self.uyy[i] += 1
           self.uzz[i] -= 1
        elif dir6 == 25:
           self.uxx[i] -= 1
           self.uyy[i] += 1
           self.uzz[i] += 1
        elif dir6 == 26:
           self.uxx[i] += 1
           self.uyy[i] -= 1
           self.uzz[i] -= 1  
           
    def conflicts(self,i,D):
        if (D == 1):
         if (self.uxx[i]==self.preX.any()):
             self.uxx[i]=self.preX[i]
             return 1
         else:
             return 0
        elif (D == 2):
         if (self.uxx[i]==self.preX.any() and self.uyy[i]==self.preY.any()):
            self.uxx[i]=self.preX[i]
            self.uyy[i]=self.preY[i]
            return 1
         else:
            return 0
        elif (D == 3):
         if (self.uxx[i]==self.preX.any() and self.uyy[i]==self.preY.any()):
             self.uxx[i]=self.preX[i]
             self.uyy[i]=self.preY[i]
             self.uzz[i]=self.preZ[i]
             return 1
         else:
            return 0
    
    
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
                 self.preX = self.uxx  
                 dir1 = random.choice((1,2))
                 if dir1 == RIGHT:
                   self.uxx[i] += 1
                 elif dir1 == LEFT:
                    self.uxx[i] -= 1
               if (self.type == 'b'):
                   self.conflicts(i,1)
        
                   
         #self.xcor.append(uxx)
         #print("xcor",self.xcor)
    def move2d(self,np,ns,p0):
        #RIGHT = 1; LEFT = 2; UP = 3; DOWN = 4; UP_RIGHT = 5; UP_LEFT = 6;
        #DOWN_RIGHT = 7;DOWN_LEFT = 8
        self.prob4move = 4*(1-(p0))*p0
        self.prob8move = 4*(p0*p0)
        for  step in range (ns):
            for i in range (np):
                if (self.x <= self.prob4move):
                    self.preX = self.uxx
                    self.preY = self.uyy
                    self.move_dir2(i)
                    if(self.type =='b'):                    
                       if(self.conflicts(i,2)):
                           i=i-1
                   
                elif(self.x <= self.prob4move+self.prob8move):
                    self.preX = self.uxx
                    self.preY = self.uyy
                    self.move_dir3(i)
                    if(self.type == 'b'):
                       if(self.conflicts(i,2)):
                           i=i-1
                    
    def move3d(self,np,ns,p0):
        self.probnomove3D = (1-2*p0)**3
        self.prob1axis3D = 6*(((1-2*p0)**2)*p0)
        self.prob2axis3D = 12*(((1-2*p0)*p0**2))
        self.prob3axis3D = 8*((p0)**3)
        for step in range(ns):
            for i in range(np):
                if(self.x <= self.prob1axis3D):
                   self.preX = self.uxx
                   self.preY = self.uyy
                   self.preZ = self.uzz
                   self.move_dir4(i)
                   if(self.type == 'b'):
                      self.conflicts(i,3)
                
                elif(self.x <= self.prob1axis3D+self.prob2axis3D):
                   self.preX = self.uxx
                   self.preY = self.uyy
                   self.preZ = self.uzz
                   self.move_dir5(i)
                   if(self.type == 'b'):
                      self.conflicts(i,3)

                elif(self.x <= self.prob1axis3D+self.prob2axis3D+self.prob3axis3D):
                   self.preX = self.uxx
                   self.preY = self.uyy
                   self.preZ = self.uzz 
                   self.move_dir6(i)
                   if(self.type == 'b'):
                      self.conflicts(i,3)

           
    
tstart = time.time()        
v = Particle()
b = Particle()
#b = Particle()
v.settype('v')
v.nomove(10)
plt.scatter(v.uxx,v.uyy)
plt.show()
b.settype('b')
b.nomove(10)
plt.scatter(b.uxx,b.uyy,c='r')
plt.show()
v.move2d(10,10,0.2)
b.move2d(10,10,0.2)
tfinish = time.time()
print ("the average time using numpy:", tfinish-tstart, "s")
plt.scatter(v.uxx,v.uyy)
plt.show()
plt.scatter(b.uxx,b.uyy,c='r')
plt.show()
plt.scatter(v.uxx,v.uyy)
plt.scatter(b.uxx,b.uyy,c='r')
plt.show()
#plt.scatter(uyy,uzz)
#plt.show()
#plt.scatter(uxx,uzz)
#plt.show()


                    
                    
                    
                 
           
              
         
        