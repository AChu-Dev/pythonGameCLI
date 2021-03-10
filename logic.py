 
def createCharacter(playerObj):   
    print("Lets set about creating your character...\n")
    
    #Set Gender
    print("What is your gender?")
    print("Your options are:\n1)Male\n2)Female\n3)Other")
    response = int(input("Please Input a corresponding number:  "))
    if(response == 1):
        playerObj.setGender("Male")
    elif(response == 2):
        playerObj.setGender("Female")
    else:
        playerObj.setGender("Other")
    
    #Set Name
    firstName = input("What is your first name?:    ").title()
    lastName = input("What is your last name?:  ").title()
    playerObj.setFirstName(firstName)
    playerObj.setLastName(lastName)
    
    #Set Race
    print("What race would you like to be?")
    print("The races are:\n")
    print("1)HUMAN\nThese are non-occult beings so they get the following traits:\nOccultism -1\nMana is capped at 3")
    print("\n2)MAGUS\nThese are practitioners of occult Magecraft and have these traits:\nOccultism +1\nHealth +1\nMana +2")
    print("\n3)ATLAS ALCHEMIST\nThese are practitioners of Alchemy and are known for their use of technology rather than magecraft:\nOccultism +1\nAcademics +3\nAthletics -1\nMana +1")
    print("\n4)CHURCH EXECUTIONER\nThese are pious believers in the Church and have these traits:\nOccultism -1\nAcademics +2\nAthletics +1")
    print("\n5)HOMMUNCLUS\nThese are beings created by the use of Alchemy and have these traits:\nOccultism +2\nHealth -3\nCharm +2\nMana  +5")
    print("\n6)DEAD APOSTLE (VAMPIRE)\nThese are the undead offspring of the Crimson Moon and have these traits:\nOccultism +2\nAthletics +2\nMana +3\nBut they come with a drawback called the 'Curse of Decay' forcing them to drink human blood regularly")

    #Skill Assignment
    response = int(input("\nPlease Input a corresponding number:  "))
    array = []
    if(response == 1):
        playerObj.setRace("Human")
        print("\nHumans can only have the basic 1)'Reinforcement' magecraft as a skill")
        print("But they can have a variant, 2)'The Mystic Eyes of Death Perception' \nThis comes with a new statistic called Sanity as a demerit")
        inputtedSet = set(input("Please input which skills you would like in the format x, y:   "))
        for x in inputtedSet:
            if x == "1":
                array.append(1)
            elif x == "2":
                array.append(2)
        if len(array) >= 1:
            playerObj.setPlayerSkillId(array)
        else:
            responseStr = input("You have no skills selected, is this correct? (Y/N)")
            if responseStr.lower() == "y" or  responseStr.lower() == "yes":
                playerObj.setPlayerSkillId(array)
            else:
                print("You have inputted something unexpected") 

    elif(response == 2):
        playerObj.setRace("Magus")
        print("\nMagus have a large selection of magecrafts that are possible to learn, but you can only up to learn three:\n1) Gandr\n2)Reinforcement\n3)Golemancy\n4)Necromancy\n5)ElementalMagics")
        inputtedSet = set(input("Please input which skills you would like in the format x, y, z:   "))
        for x in inputtedSet:
            if x == "1" or x == 1:
                array.append(0)
            elif x == "2" or x == 2:
                array.append(1)
            elif x == "3" or x == 3:
                array.append(2)
            elif x == "4" or x == 4:
                array.append(3)
            elif x == "5" or x == 5:
                array.append(6)
        if len(array) >= 1:
            playerObj.setPlayerSkillId(array)
        else:
            response = input("You have no skills selected, is this correct? (Y/N)")
            if response.lower() == "y" or response.lower() == "yes":
                playerObj.setPlayerSkillId(array)

    elif(response == 3):
        playerObj.setRace("Atlas Alchemist")
        print("\nAlchemists have a large selection of skills please choose two skills:\n1)Reinforcement\n2)Divination\n3)Alchemy")
        inputtedSet = set(input("Please input which skills you would like in the format x, y:   "))
        for x in inputtedSet:
            if x == "1" or x == 1:
                array.append(1)
            elif x == "2" or x == 2:
                array.append(5)
            elif x == "3" or x == 3:
                array.append(7)
        if len(array) >= 1:
            playerObj.setPlayerSkillId(array)
        else:
            response = input("You have no skills selected, is this correct? (Y/N)")
            if response.lower() == "y" or response.lower() == "yes":
                playerObj.setPlayerSkillId(array)

    elif(response == 4):
        playerObj.setRace("Church Executioner")
        print("\nChurch Executioners have two skills, please choose two skills to use:\n1)Reinforcement\n2)Church Rites")
        inputtedSet = set(input("Please input which skills you would like in the format x, y:   "))
        for x in inputtedSet:
            if x == "1" or x == 1:
                array.append(1)
            elif x == "2" or x == 2:
                array.append(4)
        if len(array) >= 1:
            playerObj.setPlayerSkillId(array)
        else:
            response = input("You have no skills selected, is this correct? (Y/N)")
            if response.lower() == "y" or response.lower() == "yes":
                playerObj.setPlayerSkillId(array)

    elif(response == 5):
        playerObj.setRace("Hommunclus")
        print("\nHommuncli have two skills, please choose two skills to use:\n1)Reinforcement\n2)Alchemy")
        inputtedSet = set(input("Please input which skills you would like in the format x, y:   "))
        for x in inputtedSet:
            if x == "1" or x == 1:
                array.append(1)
            elif x == "2" or x == 2:
                array.append(7)
        if len(array) >= 1:
            playerObj.setPlayerSkillId(array)
        else:
            response = input("You have no skills selected, is this correct? (Y/N)")
            if response.lower() == "y" or response.lower() == "yes":
                playerObj.setPlayerSkillId(array)


    elif(response == 6):
        playerObj.setRace("Dead Apostle")
        print("\nDead Apostles have four skills, please choose three skills to use:\n1)Reinforcement\n2)Mystic Eyes of Enchantment\n3)Vampiric Claws\n4)Necromancy")
        inputtedSet = set(input("Please input which skills you would like in the format x, y:   "))
        for x in inputtedSet:
            if x == "1" or x == 1:
                array.append(1)
            elif x == "2" or x == 2:
                array.append(9)
            elif x == "3" or x == 3:
                array.append(10)
            elif x == "4" or x == 4:
                array.append(3)
        if len(array) >= 1:
            playerObj.setPlayerSkillId(array)
        else:
            response = input("You have no skills selected, is this correct? (Y/N)")
            if response.lower() == "y" or response.lower() == "yes":
                playerObj.setPlayerSkillId(array)
    else:
        print("You set something out of range")


def day():
    
