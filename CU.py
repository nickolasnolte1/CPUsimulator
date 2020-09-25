import IntegratedCircuit
from RAM import Ram 
from Registers import Registers
from ROM import Rom
from ALU import Alu 

class CU:

    def __init__ (self):
        self.fetch = RAM.getCode(self)
        

    def __str__(self): 
        return f"{self.fetch}"
    
    #def doFetch (self):
        #return self.fetch

    def decode(self, instruct, location):
        self.instruct = instruct
        self.location = location

        if (instruct == 'OutputToRam'):
            print("no entendi que hace")
        elif (instruct == 'RamToR0'):
            Do = self.r0[0] = self.location
        elif (instruct == 'RamToR1'):
            Do = self.r1[0] = self.location
        elif (instruct == 'DoesAND'):
            Do = 'and'
        elif (instruct == 'ReadConstantToR0'):
            Do = ''
        


    #def execute (self):
        #pass

ejemplo = CU()
print(ejemplo)