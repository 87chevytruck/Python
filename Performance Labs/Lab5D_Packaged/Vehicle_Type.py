""" Ricky Smith, Lab5D:  Automotive Class, 14 Sep 2018 """

# create Vehicle Type class
class Vehicle_Type:
    def __init__(self, vType):
        def getVehicleType():
            if vType == "truck":
                return "truck"
            elif vType == "car":
                return "car"
            elif vType == "SUV":
                return "SUV"
            elif vType == "van":
                return "van"
            else:
                return "ERROR:  Incorrect Vehicle Type Entered"

class Engine:
    def __init__(self, numCylinders, HP, TQ):
        self.numCylinders = numCylinders
        self.HP = HP
        self.TQ = TQ
    
    def setNumCylinders(self, numCylinders):
        if numCylinders < 2:
            return "ERROR:  Too few cylinders chosen."
        elif numCylinders > 12:
            return "ERROR:  Too many cylinders chosen."
        else:
            self.numCylinders = numCylinders
    
    def getNumCylinders(self):
        return self.numCylinders
    
    def setHP(self, HP):
        if HP > 1500:
            return "ERROR:  Too much power."
        elif HP < 50:
            return "ERROR:  Too little power."
        else:
            self.HP = HP

    def getHP(self):
        return self.HP

