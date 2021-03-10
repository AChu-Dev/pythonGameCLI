from player import player
#from servant import servant
from skills import skills
import logic

def intro():
    introCounter = True
    while(introCounter):
        print("Welcome to a fanmade Fate/ Text Based Game")
        print("Your options are:\n1)New Game\n2)Load Game\nExit Game")
        response = int(input("Please Input a corresponding number:  "))
        playerState = ""
        worldState = ""
        playerObj = player()
        worldObj = world()
        if(response == 1):
            playerSave = open("playerSave.txt", "w+")
            playerSave.close()
            stateSave = open("stateSave.txt", "w+")
            stateSave.close()
            print("New Save has been created")
            logic.createCharacter(playerObj)
            logic.createWorld(worldObj)
        elif(response == 2):
            playerSave = open("playerSave.txt", "r")
            stateSave = open("stateSave.txt", "r")
            playerState = playerSave.read()
            worldState = stateSave.read()
            #Need to build Objects from stored data -- unfinished
        elif(response == 3):
            introCounter = False
            break
        else:
            print("You Inputted something out of the conditions")
        return playerObj, worldObj   
        


    
         
#Main.py Here
#RUN Introduction Splash Menu
gameStates = intro()
playerInfo = gameStates[0]
worldInfo = gameStates[1]
   
    

        

    



