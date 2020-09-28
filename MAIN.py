from ALU import Alu
from clock import CPUclock
from Memory import Memory
from RAM import Ram
from ROM import Rom
from Registers import Registers
from CU import CU

class Main:

    def __init__ (self):
        self.alu = Alu()
        self.clock = CPUclock()
        self.memory = Memory()
        self.ram = Ram()
        self.rom = Rom()
        self.registers = Registers()
        self.cu = CU()