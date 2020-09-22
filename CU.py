import IntegratedCircuit

class CU (IntegratedCircuit):

    def __init__ (self, InstructionReg, InstAddReg):
        self.InstructionReg = InstructionReg
        self.InstAddReg = InstAddReg

    
    def fetch (self):
        pass

    def decode(self):
        pass

    def execute (self):
        pass
