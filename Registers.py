import IntegratedCircuit

class Registers():

        def __init__ (self, place):
            self.place = place

        def reg0(self):
            self.r0 = []
        
        def reg1(self):
            self.r1 = []

        def reg2(self):
            self.r2 = []

        def reg3(self):
            self.r3 = []

        def pc(self):
            self.iar = []

        def inputreg(self):
            self.input = []

        def outputreg(self):
            self.out = []