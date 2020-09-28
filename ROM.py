import yaml
import Registers

class Rom:

    def __init__(self, opcode, operand):
        self.opcode = opcode
        self.operand = operand

        with open ('bios.yaml', 'r') as biosxs:
            self.bios = yaml.full_load(bios)
        
        for toDo in self.bios:
            pass

    def ramtable (self):
        p0 = self.bios['RAM']['data'][0]
        p1 = self.bios['RAM']['data'][1]
        p2 = self.bios['RAM']['data'][2]
        p3 = self.bios['RAM']['data'][3]
        p4 = self.bios['RAM']['data'][4]
        p5 = self.bios['RAM']['data'][5]
        p6 = self.bios['RAM']['data'][6]
        p7 = self.bios['RAM']['data'][7]
        p8 = self.bios['RAM']['data'][8]
        p9 = self.bios['RAM']['data'][9]
        p10 = self.bios['RAM']['data'][10]
        p11 = self.bios['RAM']['data'][11]
        p12 = self.bios['RAM']['data'][12]
        p13 = self.bios['RAM']['data'][13]
        p14 = self.bios['RAM']['data'][14]
        p15 = self.bios['RAM']['data'][15]

        self.data = {}
        self.data['0'] = p0
        self.data['1'] = p1
        self.data['2'] = p2
        self.data['3'] = p3
        self.data['4'] = p4
        self.data['5'] = p5
        self.data['6'] = p6
        self.data['7'] = p7
        self.data['8'] = p8
        self.data['9'] = p9
        self.data['10'] = p10
        self.data['11'] = p11
        self.data['12'] = p12
        self.data['13'] = p13
        self.data['14'] = p14
        self.data['15'] = p15

        print(self.data)


    def istOpcode (self):
        if (self.opcode == '0000' or 'OUTPUT' or'OUT'):
            instruct = 'OutputToRam'
        elif (self.opcode == '0001' or 'LOAD_R0' or 'LD_R0'):
            instruct = 'RamToR0'
        elif (self.opcode == '0010' or 'LOAD_R1' or 'LD_R1'):
            instruct = 'RamToR1'
        elif (self.opcode == '0011' or 'AND'):
            instruct = 'DoesAND'
        elif (self.opcode == '0100' or 'ILD_R0'):
            instruct = 'ReadConstantToR0'
        elif (self.opcode == '0101' or 'STR_R0' or 'STORE_R0'):
            instruct = 'FromR0ToRAM'
        elif (self.opcode == '0110' or 'STR_R1' or 'STORE_R1'):
            instruct = 'FromR1ToRAM'
        elif (self.opcode == '0111' or 'OR'):
            instruct = 'PerformsOR'  
        elif (self.opcode == '1000' or 'ILD_R1'):
            instruct = 'ReadContantToR1'
        elif (self.opcode == '1001' or 'ADD'):
            instruct = 'AddTwoRegs'
        elif (self.opcode == '1010' or 'SUB'):
            instruct = 'SubstractTwoRegs'
        elif (self.opcode == '1011' or 'JMP' or 'JUMP'):
            instruct = 'Jump'
        elif (self.opcode == '1100' or 'JMP_N' or 'JUMP_NEG'):
            instruct = 'NegativeAluJump'
        elif (self.opcode == '1101'):
            instruct = 'Inventado'
        elif (self.opcode == '1110'):
            instruct = 'Inventado'
        elif (self.opcode == '1111' or 'HALT' or 'HLT'):
            instruct = 'ProgramDone'
        return instruct


    def convertOperand(self):
        if (self.operand == '0000' or '0'):
            location = self.data['0']
        elif (self.operand == '0001' or '1'):
            location = self.data['1']
        elif (self.operand == '0010' or '2'):
            location = self.data['2']
        elif (self.operand == '0011' or '3'):
            location = self.data['3']
        elif (self.operand == '0100' or '4'):
            location = self.data['4']
        elif (self.operand == '0101' or '5'):
            location = self.data['5']
        elif (self.operand == '0110' or '6'):
            location = self.data['6']
        elif (self.operand == '0111' or '7'):
            location = self.data['7']
        elif (self.operand == '1000' or '8' or '10'):
            location = self.data['8']
        elif (self.operand == '1001' or '11' or '9'):
            location = self.data['9']
        elif (self.operand == '1010' or '12' or '10' or 'A'):
            location = self.data['10']
        elif (self.operand == '1011' or '13' or '11' or 'B'):
            location = self.data['11']
        elif (self.operand == '1100' or '14' or '12' or 'C'):
            location = self.data['12']
        elif (self.operand == '1101' or '15' or '13' or 'D'):
            location = self.data['13']
        elif (self.operand == '1110' or '16' or '14' or 'E'):
            location = self.data['14']
        elif (self.operand == '1111' or '17' or '15' or 'F'):
            location = self.data['15']
        return location