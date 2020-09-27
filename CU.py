from IntegratedCircuit import IntegratedCircuit
from RAM import Ram 
from Registers import Registers
from ROM import Rom
from ALU import Alu 
import sys


class CU(IntegratedCircuit):

    def __init__ (self):
        self.InsAddReg = ''
        self.upcode = " "
        self.code = ''
        self.PC = 0
        self.IAR = ''
        self.ram = Ram()
        self.registers = Registers()

        

    #def __str__(self): 
        #return f"{fetch}"


    def doFetch (self):
        fetch = self.ram.getInstruction()
        for self.PC in fetch:
            self.IAR = self.PC.split()
            self.PC =+ 1
            return self.IAR
    


    def decode(self, instruct, location):
        self.instruct = instruct
        self.location = location
        Registers()

        if (instruct == 'OutputToRam'):
            print("no entendi que hace")
        elif (instruct == 'RamToR0'):
            r0[0] = self.location
            Do = r0[0]
        elif (instruct == 'RamToR1'):
            r1[0] = self.location
            Do = r1[0]
        elif (instruct == 'DoesAND'):
            Do = 'and'
        elif (instruct == 'ReadConstantToR0'):
            Do = 'no entendi que hace'
        elif (instruct == 'FromR0ToRAM'):
            self.location = r0[0]
            Do = self.location
        elif (instruct == 'FromR1ToRAM'):
            self.location = r1[0]
            Do = self.location
        elif (instruct == 'PerformsOR'):
            Do = 'or'
        elif (instruct == 'ReadConstantToR1'):
            Do = 'no entendi'
        elif (instruct == 'AddTwoRegs'):
            Do = 'add'
        elif (instruct == 'SubstractTwoRegs'):
            Do = 'substract'
        elif (instruct == 'Jump'):
            Do = 'no entendi'
        elif (instruct == 'NegativaAluJump'):
            Do = 'negativealu'
        elif (instruct == 'Multiply'):
            Do = 'multiply'
        elif (instruct == 'Divide'):
            Do = 'divide'
        elif (instruct == 'ProgramDone'):
            Do = exit()
        return Do
            
        
        

    #def execute (self):
        #pass

    def InstructionAddressRegister(self):
        return self.InsAddReg

ejemplo = CU()
print(ejemplo.doFetch())