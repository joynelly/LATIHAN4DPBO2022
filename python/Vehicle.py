from statistics import mode


class Vehicle:

    # Constructor
    def __init__(self):
        self.fuelType = ""
        self.type = ""
        self.maxPassanger = 0
        self.age = 0
        self.model = 0
    
    def setfuelType(self, fuelType):
        self.fuelType = fuelType
    
    def getfuelType(self):
        return self.fuelType
    
    def settype(self, type):
        self.type = type
    
    def gettype(self):
        return self.type

    def setmaxPassanger(self, maxPassanger):
        self.maxPassanger = maxPassanger

    def getmaxPassanger(self):
        return self.maxPassanger
    
    def setAge(self, age):
        self.age = age

    def getAge(self):
        return self.age

    def setModel(self, model):
        self.model = model
    
    def getModel(self):
        return self.model

    def move(self):
        print(">> This " + str(self.type) + " is moving! <<")
    
    def showVehicle(self):
        print("Vehicle Type  : " + str(self.type))
        print("Vehicle Model : " + str(self.model))
        print("Age           : " + str(self.age) + " years")
        print("Fuel Type     : " + str(self.fuelType))
        print("Max Passanger : " + str(self.maxPassanger))
