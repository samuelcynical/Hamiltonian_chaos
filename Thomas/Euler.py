#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 14:23:11 2022

@author: toliveira
"""

import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from scipy.integrate import quad
from sympy import Derivative,Function,dsolve
from sympy.tensor.array import derive_by_array
from mpl_toolkits import mplot3d
import pickle


#%%


def r(x,y,z):
    return (x**2+y**2+z**2)**(1/2)
def v(vx,vy,vz):
    return (vx**2+vy**2+vz**2)**(1/2)

def acc(x,y,z):
    ax=-x/((x**2+y**2+z**2)**(3/2))
    ay=-y/((x**2+y**2+z**2)**(3/2))
    az=-z/((x**2+y**2+z**2)**(3/2))
    return ax,ay,az

def pos(x,y,z,vx,vy,vz,ax,ay,az):
    x+=vx*h
    y+=vy*h
    z+=vz*h
    vx+=ax*h
    vy+=ay*h
    vz+=az*h
    a=acc(x,y,z)
    ax=a[0]
    ay=a[1]
    az=a[2]
    return x,y,z,vx,vy,vz,ax,ay,az
#%%    Initial condition
h=0.00001    #If the step is too big,The orbit will not be normal : 0.00001 is cool
x=1
y=0.1
z=0.01
vx=0
vy=1.2
vz=0.2
ax,ay,az=acc(x,y,z)
#print(ax)
#position=pos(x,y,z,vx,vy,vz,ax,ay,az)
#print(position[0])
incrementation=0
index=[0]
x2=[x]
y2=[y]
z2=[z]
vx2=[vx]
vy2=[vy]
vz2=[vz]
ax2=[ax]
ay2=[ay]
az2=[az]
t=0
bo=1

#%%
while bo==1:
    incrementation +=1
    index.append(incrementation)
    position=pos(x,y,z,vx,vy,vz,ax,ay,az)
    x2.append(position[0])
    x=position[0]
    y2.append(position[1])
    y=position[1]
    z2.append(position[2])
    z=position[2]
    vx2.append(position[3])
    vx=position[3]
    vy2.append(position[4])
    vy=position[4]
    vz2.append(position[5])
    vz=position[5]
    ax2.append(position[6])
    ax=position[6]
    ay2.append(position[7])
    ay=position[7]
    az2.append(position[8])
    az=position[8]
    t+=h
    if r(x,y,z)<0.01:       #If we are too much close to the center, stop the loop
        print("Boom")
        bo=2
        
    if t>100:               #Just too stop at a certain time
        print("Time's up!")
        bo=2
        
        
#%%   Dumping data
f=open("/adhome/t/to/toliveira/M1/Projet/data.txt","wb")    #Put your own path 

pickle.dump(index,f)
pickle.dump(x2,f)
pickle.dump(y2,f)
pickle.dump(z2,f)
pickle.dump(vx2,f)
pickle.dump(vy2,f)
pickle.dump(vz2,f)
f.close()


#%%       Finding when it cross the plane y=0,z>0
def find_nearest(liste,value):
    liste=np.asarray(liste)
    idx=(np.abs(liste-value)).argmin()
    return liste[idx]
#print(find_nearest(y2,0))


#%%

axx=plt.axes(projection='3d')
#plt.plot(x2,y2,z2)
axx.plot3D(x2,y2,z2)
plt.show()


    
    
    
    
    
    