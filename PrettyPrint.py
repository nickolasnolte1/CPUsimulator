#from ROM import Rom
#from CU import CU
#from Registers import Registers

class PrettyPrint():

    def __init__(self):
        self.pprint =''

    def drawing(self):
        self.pprint = input("press 1 to print the CPU's current state")
        if(self.pprint == '1'):
            print("----------     ----------     ----------     ----------                                         ~R A M~")
            print("|   R0    |    |    R1   |    |   R2    |    |    R3   |------------------------------------|adress  data |")
            print("|         |    |         |    |         |    |         |                                    |      |      |")
            print("----------     ----------     ----------     -----------                                    |      |      |")
            print("     |              |                |            |                                         |      |      |")
            print("     |               --------------   ----        |                                         |      |      |")
            print("     ----------------------------  |      |       |                                         |      |      |")
            print("                                 | |      |       |                                         |      |      |")
            print("                                **************************************                      |      |      |")
            print("                                * Control Unit                       *                      |      |      |")
            print("                                *                                    *                      |      |      |")
            print("                                *             --------------         *                      |      |      |")
            print("    -------------------         *            | opcode|operand |      *                      |      |      |")
            print("     \    ALU        /          *            |       |        |      *                      |      |      |")
            print("      \             /           *             ---------------        *                      |      |      |")
            print("       \           /            *    inst.addr.reg                   *                      |      |      |")
            print("        \         /             *   -----------------                *                      |      |      |")
            print("         \       /              *  |                 |               *                      |      |      |")
            print("          \     /               *  |                 |               *                      ---------------")
            print("           \___/                **************************************")


