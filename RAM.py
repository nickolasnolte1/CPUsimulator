class Ram:

    def __init__(self):
        #self.data = data
        self.instructions = open("cpufm.txt", "r")
        self.code = []
        for line in self.instructions: 
            if not line.strip().startswith(";"):
<<<<<<< HEAD
                instruction = line.strip()
                self.code.append(instruction)              
    
    def getInstruction(self):
=======
                upcode, operand = line.strip().split(" ", 1)
                self.code[upcode] = operand
      
                
    def getCode(self):
>>>>>>> 55562f7d83bf8450959fdd0a993fcf793e3b5c34
        return self.code
        #for instruction in self.code:
            #return instruction.split(" ", 1)
            

#SOLO PARA PROBAR 
<<<<<<< HEAD
    #def __str__(self):
        #return f"""{self.code}"""

    
#ejemplo = Ram()
#print(ejemplo.getInstruction())
=======
    def __str__(self):
        return f""" FILE:\n{self.code} """
>>>>>>> 55562f7d83bf8450959fdd0a993fcf793e3b5c34
