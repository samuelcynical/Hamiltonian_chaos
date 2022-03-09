class star() :

    def __init__(self) :
        self.v_0            = 0
        self.init_parameter = [0,0,0,0,0,0]


    def set_init_parameter(self, p0) :
        self.init_parameter[0] = p0[0]
        self.init_parameter[1] = p0[1]
        self.init_parameter[2] = p0[2]
        self.init_parameter[3] = p0[3]
        self.init_parameter[4] = p0[4]
        self.init_parameter[5] = p0[5]
        self.v_0 = (self.init_parameter[3]**2 + self.init_parameter[4]**2 + self.init_parameter[5]**2)/2


    def GetInitParameter(self) :
        return self.init_parameter
