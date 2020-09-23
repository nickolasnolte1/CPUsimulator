import IntegratedCircuit

class ALU (IntegratedCircuit):

    def __init__(self, zero, overflow, negative, OPcode, inputs):
        self.zero = zero
        self.overflow = overflow
        self.negative = negative 
        self.OPcode = OPcode
        self.inputs = inputs
        self.result = result

    def zero (self, result):
        if (self.result == 0):
            self.zero == 0
            return self.zero

    def overflow (self, result):
        if (self.result >= 15):
            self.overflow = self.result
            return self.overflow

    def negative(self, result):
        if (self.result < 0):
            self.negative = self.result
            return self.negative

    def add (self, r1, r2):
        self.result = r1 + r2
        return self.result

    def sub (self, r1, r2):
        self.result = r1 - r2
        return self.result

    def subborrow (self, r1, r2):
        
        while(r1 != 0):
            borrow = (~r1) & r2 
            self.result = r1 ^ r2             #chequear si lo hice bien
            r2 = borrow << 1
        return self.result

    def onescomplement (self, r1):
        self.result = ~r1
        return self.result

    def towscomplement (self, r1):
        self.result = ~r1 + 1
        return self.result
        

    def logicand (self, r1, r2):

        AND = r1 & r2
        return AND 
        #if r1 == 1 and r2 == 1:
        #    return 1
        #else:
        #    return 0

    def logicor (self, r1, r2):

        OR = r1 | r2
        return OR
        #if r1 == 1 or r2 == 1:
        #    return 1
        #else:
        #    return 0

    def lshift (self, r1, r2):
        left = r1 << r2
        return left

    def rshift (self, r1, r2):
        right = r1 >> r2
        return right 

    def greater (self, r1, r2):
        greater = r1 > r2
        return greater

    def less (self, r1, r2):
        less = r1 < r2
        return less 

    def greaterequal (self, r1, r2):
        greaterequal = r1 >= r2
        return greaterequal

    def lessequal (self, r1, r2):
        lessequal = r1<= r2
        return lessequal