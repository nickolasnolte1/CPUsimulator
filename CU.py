from IntegratedCircuit import IntegratedCircuit
from RAM import Ram 
#from ROM import ROM

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
    

    def decode(self):
        pass

    #def execute (self):
        #pass

    def InstructionAddressRegister(self):
        return self.InsAddReg

ejemplo = CU()
print(ejemplo.doFetch())