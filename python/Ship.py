import imp
from Vehicle import Vehicle

class Ship(Vehicle):

    # Constructor
    def __init__(self):
        self.countryOfManufacture = ""
        self.speed = 0
        self.cruisingRange = 0
        self.endurance = 0
    
    def setcountryOfManufacture(self, countryOfManufacture):
        self.countryOfManufacture = countryOfManufacture
    
    def getcountryOfManufacture(self):
        return self.countryOfManufacture
    
    def setspeed(self, speed):
        self.speed = speed
    
    def getspeed(self):
        return self.speed

    def setcruisingRange(self, cruisingRange):
        self.cruisingRange = cruisingRange

    def getcruisingRange(self):
        return self.cruisingRange
    
    def setendurance(self, endurance):
        self.endurance = endurance

    def getendurance(self):
        return self.endurance
    
    def showShip(self):
        print("Country Of Manufacture  : " + str(self.countryOfManufacture))
        print("Speed                   : " + str(self.speed) + " knots")
        print("Cruising Range          : " + str(self.cruisingRange) + " miles")
        print("Endurance               : " + str(self.endurance) + " days")
