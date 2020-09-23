class RAM:

    def __init__(self, data):
        self.data = data
        self.instructions = open("cpufm.txt", "r")
        self.code = {}
        for line in self.instructions: 
            if not line.strip().startswith(";"):
                upcode, operand = line.strip().split(" ", 1)
                self.code[upcode] = operand
                
#SOLO PARA PROBAR 
    def __str__(self):
        return f""" FILE:\n{self.code} """

    
ejemplo = RAM("hola")
print(ejemplo)