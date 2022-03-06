class Person:

    #contructor
    def __init__(self):
        self.NIK = ""
        self.Name = ""
        self.Gender = ""
    
    def setNIk(self, nik):
        self.NIK = nik
    
    def getNIK(self):
        return self.NIK
    
    def setName(self, name):
        self.Name = name
    
    def getName(self):
        return self.Name

    def setGender(self, gender):
        self.Gender = gender

    def getGender(self):
        return self.Gender

    def sleep(self):
        print(">> " + str(self.Name) + " is sleeping! <<")
    
    def showPerson(self):
        print("NIK          : " + str(self.NIK))
        print("Name         : " + str(self.Name))
        print("Gender       : " + str(self.Gender))
