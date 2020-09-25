class Ram:

    def __init__(self):
        #self.data = data
        self.instructions = open("cpufm.txt", "r")
        self.code = []
        for line in self.instructions: 
            if not line.strip().startswith(";"):
                instruction = line.strip()
                self.code.append(instruction)              
    
    def getInstruction(self):
        return self.code
      
                
    #def getCode(self):
        #return self.code
        #for instruction in self.code:
            #return instruction.split(" ", 1)
            

#SOLO PARA PROBAR 
    #def __str__(self):
        #return f"""{self.code}"""

    
#ejemplo = Ram()
#print(ejemplo.getInstruction())
