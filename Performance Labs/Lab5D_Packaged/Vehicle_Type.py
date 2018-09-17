""" Ricky Smith, Lab5D:  Automotive Class, 14 Sep 2018 """

# create Vehicle Type class
class Vehicle_Type:
    def __init__(self, vType):
        self.vType = vType

        def setVehicleType(self, vType):
            self.vType = vType

        def getVehicleType(self):
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

    def setTQ(self, TQ):
        if TQ > 2500:
            return "ERROR:  Too much TQ."
        elif TQ < 50:
            return "ERROR:  Too little TQ."
        else:
            self.TQ = TQ

    def getTQ(self):
        return self.TQ

class Vehicle_Abilities:
    def __init__(self, vTowing, vWeight, vDoors):
        self.vTowing = vTowing
        self.vWeight = vWeight
        self.vDoors = vDoors

    def setTowing(self, vTowing):
        if vTowing < 0:
            return "ERROR:  Tow rating must be at least 0 lbs"
        elif vTowing > 30000:
            return "ERROR:  Tow rating is too high"
        else:
            self.vTowing = vTowing
    
    def getTowing(self):
        return self.vTowing

    def setWeight(self, vWeight):
        if vWeight < 1800:
            return "ERROR:  Vehicle weight must be at least 1,800 lbs"
        elif vWeight > 30000:
            return "ERROR:  Vehicle weight must be under 30,000 lbs"
        else:
            self.vWeight = vWeight
    
    def getWeight(self):
        return self.vWeight

    def setDoors(self, vDoors):
        if vDoors < 2:
            return "ERROR:  Vehicle must have at least 2 doors"
        elif vDoors > 5:
            return "ERROR:  Vehicle must have no more than 5 doors"
        else:
            self.vDoors = vDoors
    
    def getDoors(self):
        return self.vDoors

class Vehicle_Options:
    def __init__(self, powerWindows, powerLocks, nav, premAudio, backCam, leatherSeats, heatedSeats, ventedSeats, blindSpot, autoTrans, driveTrain):
        self.powerWindows = powerWindows
        self.powerLocks = powerLocks
        self.nav = nav
        self.premAudio = premAudio
        self.backCam = backCam
        self.leatherSeats = leatherSeats
        self.heatedSeats = heatedSeats
        self.ventedSeats = ventedSeats
        self.blindSpot = blindSpot
        self.autoTrans = autoTrans
        self.driveTrain = driveTrain

    def setPowerWindows(self, powerWindows):
        if powerWindows == "Yes" or powerWindows == "yes" or powerWindows == "Y" or powerWindows == "y":
            return "Yes"
        elif powerWindows == "No" or powerWindows == "no" or powerWindows == "N" or powerWindows == "n":
            return "No"
        else:
            return "ERROR:  You must enter Yes or No"
    
    def test(self):
        print("{}").format(self.vWeight)