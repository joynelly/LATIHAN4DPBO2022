class Job:

    #contructor
    def __init__(self):
        self.NIP = ""
        self.CompanyName = ""
        self.Position = ""
    
    def setNIP(self, NIP):
        self.NIP = NIP
    
    def getNIP(self):
        return self.NIP
    
    def setCompanyName(self, CompanyName):
        self.CompanyName = CompanyName
    
    def getCompanyName(self):
        return self.CompanyName

    def setPosition(self, Position):
        self.Position = Position

    def getPosition(self):
        return self.Position
    
    def showJob(self):
        print("NIP          : " + str(self.NIP))
        print("Company Name : " + str(self.CompanyName))
        print("Position     : " + str(self.Position))
