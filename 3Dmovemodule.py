# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 02:28:40 2016

@author: nanditharajamani
"""
import random

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
            