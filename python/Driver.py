from Person import Person
from Job import Job

class Driver(Person, Job):

    #constructor
    def __init__(self):
        self.licenseID = ""
        self.activeUntil = ""
        self.vehicleType = ""
    
    def setlicenseID(self, licenseID):
        self.licenseID = licenseID
    
    def getlicenseID(self):
        return self.licenseID
    
    def setactiveUntil(self, activeUntil):
        self.activeUntil = activeUntil
    
    def getactiveUntil(self):
        return self.activeUntil

    def setvehicleType(self, vehicleType):
        self.vehicleType = vehicleType

    def getvehicleType(self):
        return self.vehicleType
    
    def showDriver(self):
        print("License ID   : " + str(self.licenseID))
        print("Active until : " + str(self.activeUntil))
        print("Vehicle Type : " + str(self.vehicleType))
