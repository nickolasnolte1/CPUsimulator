from datetime import date, datetime
import time

class IntegratedCircuit:
    def __init__(self, manu, country, description, status, date):
        self.manu = manu
        self.country = country
        self.description = description
        self.status = status
        self.date = date

        if (self.status == "Deprecated"):
            deprecated = time.gmtime(0)
            new = time.strftime("%m/%d/%Y, %H:%M:%S", deprecated)
            self.date = new
        else:
            self.date = date


    
    def __str__(self):
        return f"""
            Manufacturer: {self.manu}
            Country of Manufacturer: {self.country}
            Purpose: {self.description}
            Status: {self.status} 
            Buil-date: {self.date}
            """
