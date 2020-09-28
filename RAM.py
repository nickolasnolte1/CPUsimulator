class Ram:

    def __init__(self):
        self.instructions = open("cpufm.txt", "r")
        self.code = []
        for line in self.instructions: 
            if not line.strip().startswith(";"):
                instruction = line.strip()
                self.code.append(instruction)              
    
    def getInstruction(self):
        return self.code
      
