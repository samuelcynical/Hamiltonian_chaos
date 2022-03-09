from star_class import star
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import RK45

class test(star) :

    def __init__(self, b, c, dt) :
        super().__init__()
        self.b              = b
        self.c              = c
        self.dt             = dt
        self.position       = [[],[],[]]
        self.velocity       = [[],[],[]]
        self.xmap           = []
        self.vxmap          = []


    def GetPosition(self) :
        return self.position

    def GetVelocity(self) :
        return self.velocity

    def GetXMap(self) :
        return self.xmap

    def GetVxMap(self) :
        return self.vxmap


    def potX(self, x, y, z) :
        return (self.v_0)*(-2*x) / (x**2 +(y**2)/(self.b**2) + (z**2)/(self.c**2))

    def potY(self, x, y, z) :
        return (self.v_0)*(-2*y/(self.b**2)) / (x**2 +(y**2)/(self.b**2) + (z**2)/(self.c**2))

    def potZ(self, x, y, z):
        return (self.v_0)*(-2*z/(self.c**2)) / (x**2 +(y**2)/(self.b**2) + (z**2)/(self.c**2))

    def f(self, ) :
        return (self.v_0)*(-2*x) / (x**2 +(y**2)/(self.b**2) + (z**2)/(self.c**2)), (self.v_0)*(-2*y/(self.b**2)) / (x**2 +(y**2)/(self.b**2) + (z**2)/(self.c**2)), (self.v_0)*(-2*z/(self.c**2)) / (x**2 +(y**2)/(self.b**2) + (z**2)/(self.c**2))


    def integrate(self, tmin, tmax, p0) :
        super().set_init_parameter(p0)
        def derivatives(t, x) :
            return [x[3], x[4], x[5], self.potX(x[0], x[1], x[2]), self.potY(x[0], x[1], x[2]), self.potZ(x[0], x[1], x[2])]

        rk = RK45(derivatives, t0=tmin, y0=self.init_parameter, rtol=1e-9, t_bound=tmax, first_step=self.dt, max_step=0.001)
        i = 0
        while(rk.t < rk.t_bound):
            self.position[0].append(rk.y[0])
            self.position[1].append(rk.y[1])
            self.position[2].append(rk.y[2])
            self.velocity[0].append(rk.y[3])
            self.velocity[1].append(rk.y[4])
            self.velocity[2].append(rk.y[5])

            if i > 1 :
                if self.position[1][i-1]*self.position[1][i] < 0 and (self.velocity[0][i-1]+self.velocity[0][i])/2 > 0 :
                    self.xmap.append((self.position[0][i-1] + self.position[0][i])/2)
                    self.vxmap.append((self.velocity[0][i-1] + self.velocity[0][i])/2)

            i += 1
            rk.step()

    def rk4(self):
        """
        Fourth order integrator

        Parameters
        ----------
        r : array
            Positon and velocity vector at i-th step
        h : float
            Time step
        f : function
            Gradient of the potential according the x,y and z axis
        p1 : Parameter 1 (float, depends on the choice of the potential)
            1: M mass of the attractor
            2: rc a length of reference (does not influence on the acceleration)
            3: M mass of the attractor
        p2 : Parameter 2 (float)
            1: -
            2: b shape parameter according the y axis
            3: a dimension of the galaxy
        p3 : Parameter 3 (float)
            1: -
            2: c shape parameter according the z axis
            3: b galactic thickness
            DESCRIPTION.
        v0 : float
            Initial velocity

        Returns
        -------
        r : array
            Positon and velocity vector at (i+1)-th step

        """
        k1=h*f()
        k2=h*f(r+0.5*k1)
        k3=h*f(r+0.5*k2)
        k4=h*f(r+k3)
        r+=(k1+2*k2+2*k3+k4)/6.0
        return r
