from Vehicle import Vehicle

class Airplane(Vehicle):

    # Constructor
    def __init__(self):
        self.wingsLength = 0
        self.tailHeight = 0
        self.maxRange = 0
        self.airlines = ""
    
    def setwingsLength(self, wingsLength):
        self.wingsLength = wingsLength
    
    def getwingsLength(self):
        return self.wingsLength
    
    def settailHeight(self, tailHeight):
        self.tailHeight = tailHeight
    
    def gettailHeight(self):
        return self.tailHeight

    def setmaxRange(self, maxRange):
        self.maxRange = maxRange

    def getmaxRange(self):
        return self.maxRange
    
    def setairlines(self, airlines):
        self.airlines = airlines

    def getairlines(self):
        return self.airlines
    
    def showAirplane(self):
        print("Airlines      : " + str(self.airlines))
        print("Wings Length  : " + str(self.wingsLength) + " meters")
        print("Tail Height   : " + str(self.tailHeight) + " meters")
        print("Max Range     : " + str(self.maxRange) + " NM")
