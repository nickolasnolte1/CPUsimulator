from ROM import Rom

class Ram:

    def __init__(self):
        self.instructions = open("cpufm.txt", "r")
        self.code = []
        for line in self.instructions: 
            if not line.strip().startswith(";"):
                instruction = line.strip()
                self.code.append(instruction)      
        self.rom = Rom()
        self.data = self.rom.getData()        
    
    def getInstruction(self):
        return self.code

    def getData(self):
        return self.data

    def getValue (self, position):
        return self.data[position]

    def changeValue (self, position, value):
        self.data[position] = value
      
