from IntegratedCircuit import IntegratedCircuit

class Alu (IntegratedCircuit):
        def __init__(self, OPcode, output, inputA, inputB, zero = 0, overflow = 0, negative = 0):
        self.zero
        self.overflow
        self.negative
        self.OPcode = OPcode
        self.output = output
        self.inputA = inputA
        self.inputB = inputB


    def add (self):
        return self.inputA + self.inputB

    def sub (self):
        return self.inputA - self.inputB

    def subborrow (self):
        while(self.inputA != 0):
            borrow = (~self.inputA) & self.inputB 
            self.result = self.inputA ^ self.inputB             #chequear si lo hice bien
            self.inputB = borrow << 1
        return self.result

    def onescomplement (self):
        return ~self.inputA
        

    def towscomplement (self, r1):
        return ~self.inputA + 1
        
    def logicand (self):
        return self.inputA & self.inputB

    def logicor (self):
        return self.inputA | self.inputB 

    def lshift (self):
        return self.inputA << self.inputB

    def rshift (self):
        return self.inputA >> self.inputB 

    def greater (self):
        return self.inputA > self.inputB

    def less (self,):
        return self.inputA < self.inputB 

    def greaterequal (self):
        return self.inputA >= self.inputB

    def lessequal (self):
        return self.inputA <= self.inputB

    def multiply (self, r1, r2):
        return self.inputA * self.inputB

    def divide (self, r1, r2):
        return self.inputA / self.inputB

    def calculate (self, output):
        self.output = output
        if (self.output == 0):
            return self.zero == 1
        elif (self.output > 15):
            return self.overflow == 1
        elif (self.output < 0):
            return self.negative == 1

    def zero (self, result):
        return self.zero

    def overflow (self, result):
        return self.overflow

    def negative(self, result):
        return self.negative