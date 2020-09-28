from ROM import Rom
from CU import CU
from Registers import Registers

class PrettyPrint():

    def __init__(self):
        self.pprint =''

    def drawing(self):
        self.pprint = input("press 1 to print the CPU's current state")
        if(self.pprint == '1'):
            print("      ----------     ----------     ----------    -----------                                         ~R A M~")
            print("      |  R0    |     |   R1   |    |   R2    |    |    R3   |------------------------------------|adress  data |")
            print(f"     |        |     |        |    |         |    |         |                                    |      |      |")
            print(f"     ----------     ----------    ----------     -----------                                    |      |      |")
            print(f"         |              |                 |           |                                         |      |      |")
            print(f"         |               --------------¬   ---¬       |                                         |      |      |")
            print(f"         ---------------------------¬  |      |       |                                         |      |      |")
            print(f"                                     | |      |       |                                         |      |      |")
            print(f"                                    **************************************                      |      |      |")
            print(f"                                    * Control Unit                       *                      |      |      |")
            print(f"                ------------------- *                                    *                      |      |      |")
            print(f"                |    |              *             --------------         *                      |      |      |")
            print(f"        -------------------         *            | opcode|operand |      *                      |      |      |")
            print(f"         \     ALU       /          *            |       |        |      *                      |      |      |")
            print(f"          \             /           *             ---------------        *                      |      |      |")
            print(f"           \           /            *                                    *                      |      |      |")
            print(f"            \         /             *            -----------------       *                      |      |      |")
            print(f"             \       /              *           |  inst.addr.reg  |      *                      |      |      |")
            print(f"              \     /               *           |                 |      *                      ---------------")
            print("                \___/                **************************************")
            print("                  |                        |                           |")
            print("                   ------------------------                            |")
            print("                                                                 ------------")
            print("                                                                 | clock      |")
            print(f"                                                                |            |")
            print("                                                                 ------------")
