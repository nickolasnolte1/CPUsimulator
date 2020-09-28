from IntegratedCircuit import IntegratedCircuit

class Registers(IntegratedCircuit):

    def __init__ (self):
        self.place = ''
        self.r0 = int
        self.r1 = int
        self.r2 = int
        self.r3 = int
        self.iar = int
        self.inpt = int
        self.outpt = int
        self.regAdress = ['00', '01', '10', '11']

    def getRegAdress (self, operand):
        if (operand == "R0"):
           address = 0
        elif (operand == "R1"):
            address = 1
        elif (operand == "R2"):
            address = 2
        if (operand == "R3"):
            address = 4
        return address


    def reg0 (self):
        return self.r0

    def reg0 (self, val):
        self.r0 = val
        return self.r0

    def reg1(self):
        return self.r1

    def reg1(self, val):
        self.r1 = val
        return self.r1

    def reg2(self):
        return self.r2

    def reg2(self, val):
        self.r2 = val
        return self.r2

    def reg3(self):
        return self.r3

    def reg3(self, val):
        self.r3 = val
        return self.r3

    def pc(self):
        return self.iar

    def pc(self, val):
        self.iar = val
        return self.iar    
    
    def inputreg(self):
        return self.inpt

    def outputreg(self):
        return self.outpt