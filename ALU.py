import IntegratedCircuit

class ALU (IntegratedCircuit):

    def __init__(self, zero, overflow, negative, OPcode, inputs):
        self.zero = zero
        self.overflow = overflow
        self.negative = negative 
        self.OPcode = OPcode
        self.inputs = inputs

    def add (self, r1, r2):
        return r1 + r2

    def sub (self, r1, r2):
        return r1 - r2

    