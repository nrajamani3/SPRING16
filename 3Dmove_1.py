# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 08:55:03 2016

@author: nanditharajamani
"""
import numpy
import random
import matplotlib.pyplot as plt
import time

##RESOLVES CONFLICTS BETWEEN BACTERIA AND VIRUS##
c=0;  

def check(s,b):
    global c 
    #if(s.uxx.all()==b.uxx.all() and s.uyy.all()==b.uyy.all()):
    if((s.uxx-b.uxx).all() and (s.uyy-b.uyy).all()):
        c=1;
    else:
        c=0;

class Particle:
##INITIALIZES ATTRIBUTES OF PARTCLE VIRUS##
##CONSIDERING IT AS CLASS PARTICLE
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
         #uxx = numpy.zeros(np)
         #for i in range (np):
         #   uxx[i] = ((np)/2) 
         for step in range (ns): 
            for i in  range (np):
               if (self.x <= self.prob):
                 dir1 = random.choice((1,2))
                 if dir1 == RIGHT:
                   self.uxx[i] += 1
                 elif dir1 == LEFT:
                    self.uxx[i] -= 1
        
         #return self.uxx           
         #self.xcor.append(uxx)
         #print("xcor",self.xcor)
    def nomove(self, np):
        self.uxx = numpy.zeros(np)
        self.uyy = numpy.zeros(np)
        self.uzz = numpy.zeros(np)
        for i in range (np):
            self.uxx[i] = ((np/2))
            self.uyy[i] = ((np/2))
            self.uzz[i] = ((np/2))
            
    def move2d(self,np,ns,p0):
        self.prob4move = 4*(1-(p0))*p0
        self.prob8move = 4*(p0*p0)
        #self.uxx = numpy.zeros(np)
        #self.uyy = numpy.zeros(np)
        #for i in range (np):
        #    self.uxx[i] = ((np/2))
        #    self.uyy[i] = ((np/2))
        for  step in range (ns):
            for i in range (np):
                if (self.x <= self.prob4move):
                    self.move_dir2(i)
                elif(self.x <= self.prob4move+self.prob8move):
                    self.move_dir3(i)
        #return self.uxx, self.uyy 
    def move3d(self,np,ns,p0):
        self.probnomove3D = (1-2*p0)**3
        self.prob1axis3D = 6*(((1-2*p0)**2)*p0)
        self.prob2axis3D = 12*(((1-2*p0)*p0**2))
        self.prob3axis3D = 8*((p0)**3)
        #self.uxx = numpy.zeros(np)
        #self.uyy = numpy.zeros(np)
        #self.uzz = numpy.zeros(np)
        #for i in range(np):
        #    self.uxx[i] = (np/2)
        #    self.uyy[i] = (np/2)
        #    self.uzz[i] = (np/2)
        for step in range(ns):
            for i in range(np):
                if(self.x <= self.prob1axis3D):
                  self.move_dir4(i)
                elif(self.x <= self.prob1axis3D+self.prob2axis3D):
                  self.move_dir5(i)
                elif(self.x <= self.prob1axis3D+self.prob2axis3D+self.prob3axis3D):
                    self.move_dir6(i) 
##FUNCTION DEFINITIONS FOR MOVING,MAKES FOR CLEANER CODE##    
    
    
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
           
        
    
tstart = time.time()        
#INITIAL PLOT,CONSIDER VIRUS AND BACTERIA TO HAVE SAME ATTRIBUTES##
##ASSIGNED SAME PROBABILITY OF MOVEMENT FOR BACTERIA AND VIRUS, JUST TO CHECK FOR RESOLUTION OF CONFLICTS##
s = Particle()
b = Particle()
#uxx,uyy,uzz = s.move3d(1000,1000,0.2)
s.nomove(1000) #initializes the array for holding x y and Z coordinates
b.nomove(1000)
for i in range(1000):
    s.move2d(1000,1000,0.2)
    check(s,b);
    if(c==1):
        i=i-1
        continue;
    b.move2d(1000,1,0.3) #must determine probabilitites 
#b.move2d(1000,1000,0.1)
tfinish = time.time()
print ("the average time using numpy:", tfinish-tstart, "s")
plt.hist(s.uxx)
plt.show()
plt.scatter(s.uxx,s.uyy,c='b')
#plt.show()
plt.scatter(b.uxx,b.uyy,c='r')
plt.show()
#plt.scatter(s.uyy,s.uzz)
#plt.show()
#plt.scatter(s.uxx,s.uzz)
#plt.show()
#plt.scatter(s.uxx,b.uxx)
#plt.show()

        
        
    



                    
                    
                    
                 
           
              
         
        