class player:

    def __init__(self):
        self.gender = ""
        self.firstName = ""
        self.lastName = ""
        self.race = ""
        self.playerSkillIds = []
        self.servantClass = ""

    def setGender(self, gender):
        self.gender = gender

    def getGender(self):
        x = self.gender
        return(x)

    def setRace(self, race):
        self.race = race

    def getRace(self):
        x = self.race
        return(x)
    
    def setFirstName(self, firstName):
        self.firstName = firstName

    def getFirstName(self):
        x = self.firstName
        return(x)

    def setLastName(self, lastName):
        self.lastName = lastName

    def getLastName(self):
        x = self.lastName
        return(x)
    
    def setPlayerSkillId(self, array):
        self.playerSkillIds = array

    def getPlayerSkillId(self):
        x = self.playerSkillIds
        return(x)

    def setServantClass(self, servantClass):
        self.servantClass = servantClass

    def getServantClass(self):
        x = self.servantClass
        return(x)

    def __str__(self):
        return f'player({self.gender}, {self.race}, {self.firstName}, {self.lastName}, {self.playerSkillIds}, {self.setServantClass})'
