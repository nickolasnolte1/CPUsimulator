class Decode:

    def __init__(self, opcode, operand):
        self.opcode = opcode
        self.operand = operand

    def decopcode(self):    #LOS PRINTS SE CAMBIAN CUANDO ESTE EL RAM
        if (self.opcode == '0000' or 'OUTPUT' or 'OUT'):
            print("AQUI TIENE QUE ESCRIBIR A CONSOLA ")

        if (self.opcode == '0001' or 'LOAD_R0' or 'LD_R0'):
            print("READS RAM LOCATION INTO REGISTER R0")

        if (self.opcode == '0010' or 'LOAD_R1' or 'LD_R1'):
            print("READS RAM LOCATION INTO REGISTER R1")

        if (self.opcode == '0011' or 'AND'):
            print("PERFORMS AND")

        if (self.opcode == '0100' or 'ILD_R0'):
            print("IMMEDIATE READ INTO R0")

        if (self.opcode == '0101' or 'STR_R0' or 'STORE_R0'):
            print("DE R0 A UN LOCATION DE RAM")
        
        if (self.opcode == '0110' or 'STR_R1' or 'STORE_R1'):
            print("DE R1 A LOCATION DE RAM")

        if (self.opcode == '0111' or 'OR'):
            print("PERFORMS OR")  

        if (self.opcode == '1000' or 'ILD_R1'):
            print("IMMEDIATE READ INTO REGISTER R1")

        if (self.opcode == '1001' or 'ADD'):
            print("ADD TWO REGISTERS AND STORE ON THE SECOND")

        if (self.opcode == '1010' or 'SUB'):
            print("SUBSTRACT TWO REGISTERS AND STORE ON THE SECOND")

        if (self.opcode == '1011' or 'JMP' or 'JUMP'):
            print("UPDATE INST.ADDR. REG TO NEW ADDRESS")

        if (self.opcode == '1100' or 'JMP_N' or 'JUMP_NEG'):
            print("IF ALU RESULT WAS NEGATIVE, UPDATE INST.ADDR. REG TO NEW ADDRESS")

        if (self.opcode == '1101'):
            print("HAY QUE INVENTARSE ALGO")

        if (self.opcode == '1110'):
            print("HAY QUE INVENTARSE ALGO")

        elif (self.opcode == '1111' or 'HALT' or 'HLT'):
            print("HALT COMPUTER")

    def decoperand(self):
        if (self.perand == '0000' or '0'):
            operando = 0

        if (self.operand == '0001' or '1'):
            operando = 1

        if (self.operand == '0010' or '2'):
            operando = 2

        if (self.operand == '0011' or '3'):
            operando = 3

        if (self.operand == '0100' or '4'):
            operando = 4

        if (self.operand == '0101' or '5'):
            operando = 5

        if (self.operand == '0110' or '6'):
            operando = 6

        if (self.operand == '0111' or '7'):
            operando = 7

        if (self.operand == '1000' or '8' or '10'):
            operando = 8

        if (self.operand == '1001' or '11' or '9'):
            operando = 9

        if (self.operand == '1010' or '12' or '10' or 'A'):
            operando = 10

        if (self.operand == '1011' or '13' or '11' or 'B'):
            operando = 11

        if (self.operand == '1100' or '14' or '12' or 'C'):
            operando = 12

        if (self.operand == '1101' or '15' or '13' or 'D'):
            operando = 13

        if (self.operand == '1110' or '16' or '14' or 'E'):
            operando = 14

        if (self.operand == '1111' or '17' or '15' or 'F'):
            operando = 15
