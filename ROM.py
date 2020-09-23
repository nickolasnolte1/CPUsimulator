import yaml

class ROM:

    def __init__(self, IST):
        self.IST = IST

        with open ('bios.yaml', 'r') as bios:
            self.bios = yaml.full_load(bios)
    
    #ejemplo de para ver
    def __str__(self):
        #for item, value in self.bios.items():
        return f"{self.bios}"

ejemplo = ROM("hola")

print(ejemplo)