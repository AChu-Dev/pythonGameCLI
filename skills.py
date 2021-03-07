class skills:
    def __init__(self, skillId, skillName, skillDesc, skillRange, skillDamage, academics, occultism, charisma, athletics, skillRoll, skillMana, skillReq):
        self.skillId = skillId
        self.skillName = skillName
        self.skillDesc = skillDesc
        self.skillRoll = skillRoll
        self.skillDamage = skillDamage
        self.skillRange = skillRange
        self.skillModifiers = [academics, occultism, charisma, athletics]
        #[Academics, Occultism, Charisma, Athletics]
        self.skillMana = skillMana
        self.skillReq = skillReq

    def getSkillId(self):
        x = self.skillId
        return(x)

    def getSkillName(self):
        x = self.skillName
        return(x)

    def getSkillDesc(self):
        x = self.skillDesc
        return(x)

    def getSkillRange(self):
        x = self.skillRange
        return(x)

    def getSkillDamage(self):
        x = self.skillRange
        return(x)
    
    def getSkillModifiers(self):
        x = self.skillModifiers
        return(x)
    
    def getSkillRoll(self):
        x = self.skillRoll
        return(x)
    
    def getskillMana(self):
        x = self.skillMana
        return(x)
    
    def getSkillReq(self):
        x = self.skillReq
        return(x)

    def __str__(self):
        return f'({self.skillId},{self.skillName},{self.skillDesc},{self.skillDamage}, {self.skillModifiers[0]}, {self.skillModifiers[1]}, {self.skillModifiers[2]}, {self.skillModifiers[3]}, {self.skillRoll}, {self.skillMana}, {self.skillReq})'


skill0 = skills(0, "Gandr", "A application of a Norse Curse, compounded with a form of Gem Magecraft which allow the user to fire magical bullets that apply the curse on impact.", 15, "3-6", 0, -1, 0, 0, "Occultism", -2, "Gem")
skill1 = skills(1, "Reinforcement", "A basic form of magecraft in which you fill mana into an object or person, which increases its basic statistics.", 0, "0", 0, 0, 0, +2, "Occultism", -1, "")
skill2 = skills(2, "Golemancy", "The use of magecraft which allows the user to craft Golems using clay and the element of Earth.", 0, "0", 0, 0, 0, 0, "Occultism", -2, "Earth")
skill3 = skills(3, "Necromancy", "This is a advanced form of Magecraft, which involves using the dead to create weapons.", 10, "4-7", 0, -1, 0, 0, "Occultism", -2, "Dead Bodies")
skill4 = skills(4, "Church Rites", "This is the form of miracles used by The Holy Churches Executioners.", 5, "5-7", 0, 0, 0, -2, "Athletics", -1, "Black Keys")
skill5 = skills(5, "Divination", "The use of astrology and tarot, to predict the future.", 0, "0", -2, 0, 0, 0, "Academics", -2, "")
skill6 = skills(6, "Elemental Magics", "This is the manipulation of the base elements (Fire, Earth, Water, Wind & Ether)", 10, "2-7", 0, -2, 0, 0, "Occultism", -3, "")
skill7 = skills(7, "Alchemy", "The concept of taking an object and using mana to change that object at an atomic level", 3, "3-5", -1,0,0,0, "Academics", -2, "Earth")
skill8 = skills(8, "Mystic Eyes of Death Perception", "A degraded form of Balor's Evil Eyes, these are able to kill anything in creation.", 0, 1000, 0, 0,0 ,-3, "Athletics", -1, "Sanity")

