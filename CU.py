import IntegratedCircuit
from RAM import RAM 

class CU:

    def __init__ (self):
        self.fetch = RAM.getCode(self)
        

    def __str__(self): 
        return f"{self.fetch}"
    
    #def doFetch (self):
        #return self.fetch

    #def decode(self):
        #pass

    #def execute (self):
        #pass

ejemplo = CU()
print(ejemplo)