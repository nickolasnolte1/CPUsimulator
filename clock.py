import time
class CPUclock:
    def _init_(self,frecuencia = 0.5): #Unidad de la frecuencia: Hertz
        self.frecuencia = frecuencia

    def tiempo(self, frecuencia):
        if (frecuencia > 0):
            self.frecuencia = 1/frecuencia
        else:
            self.frecuencia = 0
    
    def sleepScreen(self):
        time.sleep(self.frecuencia) 
