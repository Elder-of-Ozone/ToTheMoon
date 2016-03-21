import curses
from AboveTheClouds import Mechanics
import pickle
from TimeMechanics import TimeMechanics
import copy

# TO DO
#
# 1. Get length of screen.
#



def get_param(prompt_string):
     screen.clear()
     screen.border(0)
     screen.addstr(2, 2, prompt_string)
     screen.refresh()
     input = screen.getstr(10, 10, 60)
     return input

def mainMenu():
    screen.addstr(9,2, "Please enter a number:")
    screen.addstr(10,2, "1. View Planet.")
    screen.addstr(11,2, "2. View Fleet.")
    screen.addstr(12,2, "3. View Surrounding Planets.")
    screen.addstr(13,2, "4. Enter Orders (console)")
    screen.addstr(17,2, "8. About")
    screen.addstr(18,2, "9. Exit")

def viewSurroundingPlanets():
    screen.clear()
    screen.border(0)
    screen.addstr(10,5, "Surrounding Planets")
    screen.refresh()
    screen.getch()


def viewPlanetChoice():

    x = screen.getch()

    

    if x == ord("+"):
        playerList = [user, easy]
        TimeMechanics.updateEVERYTHING(playerList, planets)


        
        return True

    else: 
        return False

def viewPlanet():
    quitLoop = True
    while quitLoop == True:
        screen.clear()
        screen.border(0)
    

        userPlanet = user['planets'][0]
   # currentPlanet = planets[userPlanet]
        population = userPlanet['population']
        water = userPlanet['water']
        REE = userPlanet['REE']
        debris = userPlanet['resource']['debris']
        waterResource = userPlanet['resource']['waterResource']
        foodResource = userPlanet['resource']['foodResource']
        REEResource = userPlanet['resource']['REEResource']



        ######################
        #                    #
        #   Left Hand Side   #
        #                    #
        ######################


        screen.addstr(2,2, "Planet list.") 

        for i, planetName in enumerate(user['planets']):
            screen.addstr(4+i,2,"%d. %s" %(i+1, planetName["name"]))
        


        for i in xrange(1,27):
            screen.addstr(i,15, "#")

           #population = "200"

        screen.addstr(2, 20, "Planet Information")
        screen.addstr(4, 20, "Name:                 p1")



        screen.addstr(6, 20, "Population:           %d" % population)
        screen.addstr(7, 20, "Water Resources:      %d" % waterResource)
        screen.addstr(8, 20, "Food Resources:       %d" % foodResource)
        screen.addstr(9, 20, "Rare Earth's:         %d" % REEResource)
        screen.addstr(10,20, "Debris:               %d" % debris)




        for i in xrange(1,27):
            screen.addstr(i,51, "#")


        screen.addstr(2, 55, "Game information")
        screen.addstr(4, 55, "Time                 100 ")
        screen.addstr(5, 55, "Turns                100 ")


        screen.addstr(7, 55, "Misc")
        screen.addstr(9, 55, "Water:                %d" % water)
        screen.addstr(10, 55,"REE:                  %d" % REE)




        screen.addstr(15, 17, "   Buildings            ")
        screen.addstr(17, 17, "M. Mine:                1")
        screen.addstr(18, 17, "F. Farm:                1")
        screen.addstr(19, 17, "D. Desalination:        1")

        # Fleets section








        screen.addstr(15, 55, "Fleet Information")






        
        screen.refresh()

        quitLoop = viewPlanetChoice()

def viewFleet():
    
    #   OUTGOINGS
    #
    #   Fleet Name      Origin        Destination         Time
    #   
    #   fleet1
    #   fleet2
    #   fleet3
    #
    #
    #   INCOMING
    #   
    #   Fleet Name      Origin        Destination         Time
    #
    #   fleet1
    #   fleet2
    #   fleet3



    screen.clear()
    screen.border(0)
    screen.addstr(10,5, "viewing fleet")
    screen.refresh()
    screen.getch()

def about():
    screen.clear()
    screen.border(0)
    screen.addstr(3,2, "Write an about message regarding development")
    screen.refresh()
    screen.getch()



if __name__ == "__main__":
   
    user    = {
                "name"          : "Hydrius",
                "planets"       : None,
                "turns"         : 100,
                #"population"    : 100,
                "fighters"      : 100,
                "bombers"       : 100,
                "cargo"         : 1
            } 
    easy    = {
                "name"          : "easy",
                "planets"       : None,
                "population"    : 100,
                "fighters"      : 100,
                "bombers"       : 100,
                "cargo"         : 1
            }
    medium  = {}
    hard    = {}



    planets = {
                "p1": 
                {
                    "name": "p1",
                    "owner": "hydrius",
                    "population": 100,
                    "REE"       : 3,
                    "water"     : 3,

                    "resource": {
                            "debris"    : 100,
                            "waterResource": 500,
                            "foodResource": 500,
                            "REEResource"       : 200,
                    },
                    "building": {
                            "mine": 1,
                            "farm": 1,
                            "desalination": 1,

                        },


                    "fleetOwner": [
                        {
                         "name": "hydrius",
                         "fighters": 100,
                         "bombers" : 100,
                         "cargo"   : 1
                        }]
                 },
                
                 "p2": 
                    {
                    "name" :"p2",
                    "owner": "hydrius",
                    "REE"       : 3,
                    "water"     : 3,
                    "debris"    : 100,
                    "resource": {
                        "debris"    : 100,
                        "waterResource": 500,
                        "foodResource": 500,
                        "REEResource"       : 200,
                    },

                    "waterResource": 500,
                    "foodResource": 500,
                    "REEResource"       : 200,
                    "population": 100,
                    "fleetOwner": [
                        {
                         "name": "easy",
                         "fighters": 100,
                         "bombers" : 100,
                         "cargo"   : 1
                        }]
                 }
                }
 
    # create a pointer to planets
    user["planets"] = [copy.deepcopy(planets["p1"]), copy.deepcopy(planets["p2"])]
    easy["planets"] = [copy.deepcopy(planets["p2"])]




    TimeMechanics = TimeMechanics()
            



    x = 0

    screen = curses.initscr()
    screen.clear()
    screen.border(0)

    while x != ord('9'):


        #ASCII Name came from 
        #http://patorjk.com/software/taag/#p=display&h=1&v=1&f=Slant&t=To%20The%20Moon
        name1 = "   ______          ______ __             __  ___   "
        name2 = "  /_  __/____     /_  __// /_   ___     /  |/  /____   ____   ____ "
        name3 = "   / /  / __ \     / /  / __ \ / _ \   / /|_/ // __ \ / __ \ / __ \ "
        name4 = "  / /  / /_/ /    / /  / / / //  __/  / /  / // /_/ // /_/ // / / /"
        name5 = " /_/   \____/    /_/  /_/ /_/ \___/  /_/  /_/ \____/ \____//_/ /_/ "
                                                                                        



        message = "Welcome Captain! We await your orders!"


        #Mechanics = Mechanics.start()
        #Mechanics.start()
        #if not Mechanics.start()
        screen.clear()
        screen.border(0)
        screen.addstr(1,5, name1)
        screen.addstr(2,5, name2)
        screen.addstr(3,5, name3)
        screen.addstr(4,5, name4)
        screen.addstr(5,5, name5)

        screen.addstr(7,2, message)
        mainMenu()
        screen.refresh()
        x = screen.getch()
        
        if x == ord('1'):
            viewPlanet()
        
        if x == ord('2'):
            viewFleet()
       
        if x == ord('3'):
            viewSurroundingPlanets()

        if x == ord('4'):
            order = get_param("Enter orders")

        if x == ord('8'):
            about()

        if x == ord('+'):
            #player list should be in a class + function somewhere.
            playerList = [user, easy]
            TimeMechanics.updateEVERYTHING(playerList, planets)

        if x == ord('q'):
                break
                curses.endwin()

        screen.refresh()

curses.endwin()









