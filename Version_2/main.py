import numpy as np
import matplotlib.pyplot as plt
from star_class import star
from test import test
#from runge_class import runge
from poincaremap_class import poincare_map


#Load data from data.txt
input       = open('data.txt','r')
data_file   = input.readlines()

N   = int(data_file[0])     #Number of stars
b   = float(data_file[1])   #b parameter
c   = float(data_file[2])   #c parameter
dt  = float(data_file[3])   #Time step
T   = float(data_file[4])   #Max time

input.close()



#Generate N-objects with random initial conditions
rng             = np.random.Generator(np.random.MT19937())
star_list       = []
map_list        = []
init_condition  = []


for i in range(N) :
	init_condition.append([])
	ximpact = []
	vximpact = []

	for j in range(6) :
		init_condition[i].append(rng.random())

	#v0 = (init_condition[i][3]**2+init_condition[i][4]**2+init_condition[i][5]**2)/2
	b = rng.random()#0.4858339799268505
	while b < 0.4 :
		b = rng.random()
	c = rng.random()#0.5454313373190419
	while c > b :
		c = rng.random()

	star_object = star()
	star_list.append(star_object)
	#star_list[i].set_init_parameter()
	#star_list[i].integrate(0,T)
	map = test(b, c, dt)
	map_list.append(map)
	
	map_list[i].integrate(0,T, init_condition[i])


	'''
	map_object = poincare_map(ximpact, vximpact)
	map_list.append(map_object)
	map_list[i].ImpactPlane(star_list[i].GetPosition()[0], star_list[i].GetPosition()[1], star_list[i].GetVelocity()[0])
	'''
	print('star',i,b,c)


#Do ze drawing
fig = plt.figure()
ax  = plt.axes(projection='3d')
for i in range(N) :
	ax.plot3D(map_list[i].GetPosition()[0], map_list[i].GetPosition()[1], map_list[i].GetPosition()[2])
	#plt.plot(star_list[i].GetPosition()[0],star_list[i].GetPosition()[1])
plt.show()


for i in range(N):
	plt.scatter(map_list[i].GetXMap(), map_list[i].GetVxMap(), s = 2)
plt.show()


'''
ze  = poincare_map()
ze.parameter(star_list[0].GetXlist(),star_list[0].GetYlist())
'''
