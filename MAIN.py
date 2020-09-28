from ALU import Alu
from CU import CU
from Registers import Registers
from Clock import CPUclock
from Memory import Memory
from RAM import Ram
from ROM import Rom



class Main:

    def __init__ (self):
        self.alu = Alu()
        self.clock = CPUclock()
        self.memory = Memory()
        self.ram = Ram()
        self.rom = Rom()
        self.registers = Registers()
        self.cu = CU()
