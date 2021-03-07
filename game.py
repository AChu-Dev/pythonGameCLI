import player
import servant
import skills

global playerInfo
global worldInfo


def intro():
    introCounter = True
    while(introCounter):
        print("Welcome to a fanmade Fate/ Text Based Game")
        print("Your options are:\n1)New Game\n2)Load Game\nExit Game")
        response = int(input("Please Input a corresponding number:  "))
        if(response == 1):
            playerSave = open("playerSave.txt", "x")
            playerSave.close()
            stateSave = open("stateSave.txt", "x")
            stateSave.close()
            print("New Save has been created")
            createCharacter()
        elif(response == 2):
            playerSave = open("playerSave.txt", "r")
            stateSave = open("stateSave.txt", "r")
            playerInfo = playerSave.read()
            worldInfo = stateSave.read()
        elif(response == 3):
            introCounter = False
            break
        else:
            print("You Inputted something out of the conditions")


def createCharacter():
    playerObj = player()
    print("Lets set about creating your character...\n")

    print("What is your gender?")
    print("Your options are:\n1)Male\n2)Female\n3)Other")
    response = int(input("Please Input a corresponding number:  "))
    if(response == 1):
        playerObj.setGender("Male")
    elif(response == 2):
        playerObj.setGender("Female")
    else:
        playerObj.setGender("Other")

    firstName = input("What is your first name?:    ").title()
    lastName = input("What is your last name?:  ").title()

    playerObj.setFirstName(firstName)
    playerObj.setLastName(lastName)

    print("What race would you like to be?")
    print("The races are:\n")
    print("1)HUMAN\nThese are non-occult beings so they get the following traits:\nOccultism -1\nMana is capped at 3")
    print("But they can have a variant, 'The Mystic Eyes of Death Perception' \nThis comes with a new statistic called Sanity as a demerit")
    print("2)MAGUS\nThese are practitioners of occult Magecraft and have these traits:\nOccultism +1\nHealth +1\nMana +2\nAnd they can use Exclusive Spells")
    print("3)ATLAS ALCHEMIST\nThese are practitioners of Alchemy and are known for their use of technology rather than magecraft:\nOccultism +1\nAcademics +3\nAthletics -1\nMana +1\nThey have limited spells")
    print("4)CHURCH EXECUTIONER\nThese are pious believers in the Church and have these traits:\nOccultism -1\nAcademics +2\nAthletics +1\nCan use exclusive Church Rites skills")
    print("5)HOMMUNCLUS\nThese are beings created by the use of Alchemy and have these traits:\nOccultism +2\nHealth -3\nCharm +2\nMana  +5\nThey have limited spells as well")
    print("6)DEAD APOSTLE (VAMPIRE)\nThese are the undead offspring of the Crimson Moon and have these traits:\nOccultism +2\nAthletics +2\nMana +3\nBut they come with a drawback called the 'Curse of Decay' forcing them to drink human blood regularly")

    response = int(input("Please Input a corresponding number:  "))
    if(response == 1):
        playerObj.setRace(playerObj, "Human")
    elif(response == 2):
        playerObj.setRace(playerObj, "Magus")
    elif(response == 3):
        playerObj.setRace(playerObj, "Atlas Alchemist")
    elif(response == 4):
        playerObj.setRace(playerObj, "Church Executioner")
    elif(response == 5):
        playerObj.setRace(playerObj, "Hommunclus")
    elif(response == 6):
        playerObj.setRace(playerObj, "Dead Apostle")
    else:
        print("You set something out of range")
   
    print("Its now time to select your skills and magecraft:")
    


    
         

   
    

        

    



