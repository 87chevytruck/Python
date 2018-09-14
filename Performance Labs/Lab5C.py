""" Ricky Smith, Lab5C:  Update Hero Class, 14 Sep 2018 """

# create Person Class
class Person(object):
    def __init__(self, fName, lName, age, birthPlace):
        self.__fName = fName
        self.__lName = lName
        self.__age = age
        self.__birthPlace = birthPlace
    
    def setFname(self, fName):
        self.__fName = fName

    def getFname(self):
        return self.__fName

    def setLname(self, lName):
        self.__lName = lName

    def getLname(self):
        return self.__lName
    
    def setAge(self, age):
        self.__age = age

    def getAge(self):
        return self.__age
    
    def getBirthPlace(self):
        return self.__birthPlace

    def setBirthPlace(self, birthPlace):
        self.__birthPlace = birthPlace


# create Hero Class
class Hero(Person):
    def __init__(self, heroName, heroColor, birthPlanet):
        # Person.__init__(self, heroName)
        self.heroName = heroName
        # self.realName = person.fName + " " + person.lName
        # self.superPower = superPower
        self.heroColor = heroColor
        self.birthPlanet = birthPlanet

    def printDetails(self):
        print("Hero's Name:  {}").format(self.heroName)
        print("Hero's Real Name:  {} {}").format(self.getFname(), self.getLname())
        print("Hero's Age:  {}").format(self.getAge())
        print("Hero's Super Power:  {}").format(self.getSuperPower())
        print("Hero's Costume Color:  {}").format(self.heroColor)
        print("Hero's Birth Place:  {}").format(self.getBirthPlace())
        print("Hero's Home World:  {}").format(self.getBirthPlanet())

    def getSuperPower(self):
        return self.superPower

    def setSuperPower(self, superPower):
        self.superPower = superPower
    
    def getBirthPlanet(self):
        return self.birthPlanet

    def setBirthPlanet(self, birthPlanet):
        self.birthPlanet = birthPlanet

# set hero 1 and 2's information using the class Invisible_Hero
hero1 = Hero("The Invisible Hulk", "N/A (he's sort of invisible)", 
                       "Blackhole X-43")
hero2 = Hero("The Incredible Lady", "N/A (she's sort of invisible)", 
             "Lunar S-7")

hero1.setAge(143)
hero1.setFname("Jack")
hero1.setLname("Smith")
hero1.setSuperPower("Super Strength and Inisibility")
hero1.setBirthPlace("Secret Location")

hero2.setAge(718)
hero2.setFname("Aria")
hero2.setLname("Luna")
hero2.setSuperPower("God Like Powers (Immortal, Telekinetic, Telepathic, "
                    "Invisibility, Super Strength, etc.)")
hero2.setBirthPlace("UNKNOWN")

x1 = raw_input("What is your Hero Name?  ")
x2 = raw_input("What is your Hero's Costume Colors?  ")
x3 = raw_input("What is your Hero's Home World?  ")
x4 = raw_input("What is your Hero's Age?  ")
x5 = raw_input("What is your Hero's Real First Name?  ")
x6 = raw_input("What is your Hero's Real Last Name?  ")
x7 = raw_input("What are your Hero's Super Powers?  ")
x8 = raw_input("What is your Hero's Place of Birth?  ")

heroX = Hero(x1, x2, x3)
heroX.setAge(x4)
heroX.setFname(x5)
heroX.setLname(x6)
heroX.setSuperPower(x7)
heroX.setBirthPlace(x8)

# display hero 1 ,2 and X's info
print("= = = = = = = Hero 1 = = = = = = =")
hero1.printDetails()
print("\n= = = = = = = Hero 2 = = = = = = =")
hero2.printDetails()
print("\n= = = = = = = Hero X = = = = = = =")
heroX.printDetails()

