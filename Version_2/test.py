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
