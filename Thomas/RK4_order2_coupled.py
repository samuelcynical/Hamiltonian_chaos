import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import random




G = 6.674e-11   # gravitational constant
M = 1.267e17    # mass of Jupiter (as an example)
 # celerity?
r_c = 2

b = 0.6
c = 0.4

def a(x,y,z):																			#=derivation_of_phi=acceleration					
    d_phi_x = -(0.5*(v_0)**2)*(r_c**2/(x**2 +(y/b)**2 + (z/c)**2))*(2*x)
    d_phi_y = -(0.5*(v_0)**2)*(r_c**2/(x**2 +(y/b)**2 + (z/c)**2))*(2*y/b**2)
    d_phi_z = -(0.5*(v_0)**2)*(r_c**2/(x**2 +(y/b)**2 + (z/c)**2))*(2*z/c**2)
    return np.array([d_phi_x,d_phi_y,d_phi_z])

def Energy(x,y,z,vx,vy,vz,v_0):
    E=(1/2)*(vx**2+vy**2+vz**2)+(1/2)*(v_0**2)*np.log(x**2+(y/b)**2+(z/c)**2)
    return E

"""
    
def a(x,y,z):
	ax=-x/((x**2+y**2+z**2)**(3/2))
	ay=-y/((x**2+y**2+z**2)**(3/2))
	az=-z/((x**2+y**2+z**2)**(3/2))
	return np.array([ax,ay,az])
"""

def kx1(vx,h):
    return vx*h
def ky1(vy,h):
	return vy*h
def kz1(vz,h):
    return vz*h

def ku1(ax,h):
	return ax*h
def kv1(ay,h):
	return ay*h
def kw1(az,h):
	return az*h
	

def kx2(vx,ku1,h):
	return (vx+(1/2)*ku1)*h
def ky2(vy,kv1,h):
	return (vy+(1/2)*kv1)*h
def kz2(vz,kw1,h):
	return (vz+(1/2)*kw1)*h

def ku2(ax,h):
	return ax*h
def kv2(ay,h):
	return ay*h
def kw2(az,h):
	return az*h


def kx3(vx,ku2,h):
	return (vx+(1/2)*ku2)*h
def ky3(vy,kv2,h):
	return (vy+(1/2)*kv2)*h
def kz3(vz,kw2,h):
	return (vz+(1/2)*kw2)*h

def ku3(ax,h):
	return ax*h
def kv3(ay,h):
	return ay*h
def kw3(az,h):
	return az*h
	
def kx4(vx,ku3,h):
	return (vx+(1/2)*ku3)*h
def ky4(vy,kv3,h):
	return (vy+(1/2)*kv3)*h
def kz4(vz,kw3,h):
	return (vz+(1/2)*kw3)*h
	
def ku4(ax,h):
	return ax*h
def kv4(ay,h):
	return ay*h
def kw4(az,h):
	return az*h
	
	


def run_RK4(x0,y0,z0,v0x,v0y,v0z,h,n):

	xx=[x0]
	yy=[y0]
	zz=[z0]
	vxx=[v0x]
	vyy=[v0y]
	vzz=[v0z]
	map_x=[]
	map_x_dot=[]
	for i in range(n):
		x=xx[i]
		y=yy[i]
		z=zz[i]
		vx=vxx[i]
		vy=vyy[i]
		vz=vzz[i]
		
		ax=a(x,y,z)[0]
		ay=a(x,y,z)[1]
		az=a(x,y,z)[2]
		
		kx11=kx1(vx,h)
		ky11=ky1(vy,h)
		kz11=kz1(vz,h)
		
		ku11=ku1(ax,h)
		kv11=kv1(ay,h)
		kw11=kw1(az,h)
    	
    	
		kx22=kx2(vx,ku11,h)
		ky22=ky2(vy,kv11,h)
		kz22=kz2(vz,kw11,h)
    	
		ax=a(x+kx11/2,y+ky11/2,z+kz11/2)[0]
		ay=a(x+kx11/2,y+ky11/2,z+kz11/2)[1]
		az=a(x+kx11/2,y+ky11/2,z+kz11/2)[2]
    	
		ku22=ku2(ax,h)
		kv22=kv2(ay,h)
		kw22=kw2(az,h)
    	
    	
		kx33=kx3(vx,ku22,h)
		ky33=ky3(vy,kv22,h)
		kz33=kz3(vz,kw22,h)
    	
		ax=a(x+kx22/2,y+ky22/2,z+kz22/2)[0]
		ay=a(x+kx22/2,y+ky22/2,z+kz22/2)[1]
		az=a(x+kx22/2,y+ky22/2,z+kz22/2)[2]
    	
		ku33=ku3(ax,h)
		kv33=kv3(ay,h)
		kw33=kw3(az,h)
    	
    	
		kx44=kx4(vx,ku33,h)
		ky44=ky4(vy,kv33,h)
		kz44=kz4(vz,kw33,h)
    	
		ax=a(x+kx33/2,y+ky33/2,z+kz33/2)[0]
		ay=a(x+kx33/2,y+ky33/2,z+kz33/2)[1]
		az=a(x+kx33/2,y+ky33/2,z+kz33/2)[2]
    	
		ku44=ku4(ax,h)
		kv44=kv4(ay,h)
		kw44=kw4(az,h)
    	
    	
		X=x+(1/6)*(kx11+2*kx22+2*kx33+kx44)
		Y=y+(1/6)*(ky11+2*ky22+2*ky33+ky44)
		Z=z+(1/6)*(kz11+2*kz22+2*kz33+kz44)
		VX=vx+(1/6)*(ku11+2*ku22+2*ku33+ku44)
		VY=vy+(1/6)*(kv11+2*kv22+2*kv33+kv44)
		VZ=vz+(1/6)*(kw11+2*kw22+2*kw33+kw44)
    	
		xx.append(X)
		yy.append(Y)
		zz.append(Z)
		vxx.append(VX)
		vyy.append(VY)
		vzz.append(VZ)
		if abs(Y) <= 0.001:													#to_upgrade
			if Z>=0:
				map_x.append(X)
				map_x_dot.append(VX)
		
	return xx,yy,zz,map_x,map_x_dot,VX,VY,VZ


h=0.0000001																			#step
n=1000000000																	#total incrementation

#These are the Initial Condition
N=10
#tout=[[]*5]*N
x=1
y=0
z=0
vx=0
vy=1
vz=0.2

xx = []
yy = []
zz=[]
map_x=[]
map_x_dot=[]
E=[]
Ediff=[]
tstep=[]

for i in range(N):
    v_0=(vx**2+vy**2+vz**2)**(1/2)
    rdm =  0#float(random.uniform(-1,1))
    E.append([])
    
    
    xx.append([])
    yy.append([])
    zz.append([])
    map_x.append([])
    map_x_dot.append([])
    E[i].append(Energy(x,y,z,vx,vy,vz,v_0))
    xx[i],yy[i],zz[i],map_x[i],map_x_dot[i],vxx,vyy,vzz=run_RK4(x,y,z,vx,vy,vz,h,n)
    E[i].append(Energy(xx[i][-1],yy[i][-1],zz[i][-1],vxx,vyy,vzz,v_0))
    
    
    tstep.append(h)
    Ediff.append(abs(E[i][0]-E[i][1]))
    h=h/2
	#tout[i].insert(0,xx)
	#tout[i].insert(1,yy)
	#tout[i].insert(2,zz)
	#tout[i].insert(3,map_x)
	#tout[i].insert(4,map_x_dot)
    """
    print(map_x)    	
    print(map_x_dot)  
	print(tout[i])
	"""
    x+=rdm
    vy+=rdm
    vz+=rdm
	
fig = plt.figure()
ax  = plt.axes(projection='3d')
	
for i in range(N):	


    ax.plot3D(xx[i], yy[i], zz[i])
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    
    
"""

	
plt.scatter(map_x,map_x_dot)
plt.xlabel("x")
plt.ylabel(r"$\dot{x}$")
plt.title("Poincare section y = 0")
"""
    
    
    
plt.show()

plt.xscale('log')
plt.yscale('log')
plt.plot(tstep,Ediff,"o")
plt.show()
    

#print(tout)


"""
fig = plt.figure()
ax  = plt.axes(projection='3d')

ax.plot3D(xx, yy, zz)

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
   
plt.show()



plt.scatter(map_x,map_x_dot)
plt.xlabel("x")
plt.ylabel(r"$\dot{x}$")
plt.title("Poincare section y = 0")
plt.show()

"""
    	
    	
    	
    	
    	
    	
    	
    	
    	
    	
    	
    	
    	
    	
    	
    	
    	
    	
    
