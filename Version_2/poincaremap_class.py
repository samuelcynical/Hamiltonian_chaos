import matplotlib.pyplot as plt

class poincare_map() :

	def __init__(self, ximpact, vximpact) :
		self.ximpact  = ximpact
		self.vximpact = vximpact

	def GetXImpact(self) :
		return self.ximpact

	def GetVXImpact(self) :
		return self.vximpact

	'''
	def ImpactPlane(self, xlist, ylist, zlist, vxlist) :
		Yabs	= []
		for i in range(len(ylist)) :
			Yabs.append(abs(ylist[i]))
		i	= 0

		while i < len(ylist) :
		    if Yabs[i] <= 0.1 and zlist[i] > 0 :
		        TemporaryYlist	= []

		        while Yabs[i] <= 0.1 :
		            TemporaryYlist.append(Yabs[i])
		            i   += 1

		        self.ximpact.append(xlist[Yabs.index(min(TemporaryYlist))])
		        self.vximpact.append(vxlist[Yabs.index(min(TemporaryYlist))])

		    else:
		        i   += 1

	'''

	def ImpactPlane(self, xlist, ylist, vxlist) :
		for i in range(len(ylist)) :
			if i > 1 :
				if ylist[i-1]*ylist[i] < 0 and (vxlist[i-1]+vxlist[i])/2 > 0:
					self.ximpact.append((xlist[i-1]+xlist[i])/2)
					self.vximpact.append((vxlist[i-1]+vxlist[i])/2)


	def draw(self) :
		plt.scatter(self.ximpact, self.vximpact)
		plt.show()
