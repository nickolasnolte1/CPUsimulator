from IntegratedCircuit import IntegratedCircuit
from RAM import Ram 
from Registers import Registers
from ROM import Rom
from ALU import Alu 


class CU(IntegratedCircuit):

    def __init__ (self):
        self.InsAddReg = ''
        self.upcode = " "
        self.code = ''
        self.PC = 0
        self.IAR = ''
        self.ram = Ram()
        #self.rom = ROM()

        

    #def __str__(self): 
        #return f"{fetch}"


    def doFetch (self):
        fetch = self.ram.getInstruction()
        for self.PC in fetch:
            self.IAR = self.PC.split()
            self.PC =+ 1
            return self.IAR
    


    def decode(self, instruct, location):
        instruction = self.IAR
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

    def InstructionAddressRegister(self):
        return self.InsAddReg

ejemplo = CU()
print(ejemplo.doFetch())