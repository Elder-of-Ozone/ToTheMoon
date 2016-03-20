import curses
from AboveTheClouds import Mechanics
import pickle

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
            
def viewPlanet():
    screen.clear()
    screen.border(0)
    
    userPlanet = user['planets'][0]
    currentPlanet = planets[userPlanet]
    population = currentPlanet['population']

    #population = "200"

    for i, planetName in enumerate(user['planets']):
        screen.addstr(2+i,2,"%d. %s" %(i+1, planetName))
        
    screen.addstr(5, 60, "Population: %d" % population)


    screen.addstr(10,5, "viewing planet")
    
    screen.refresh()
    screen.getch()

def viewFleet():
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
                "planets"       : ["p1", "testPlanet"],
                "population"    : 100,
                "fighters"      : 100,
                "bombers"       : 100,
                "cargo"         : 1
            } 
    easy    = {
                "name"          : "easy",
                "Planets"       : ["p2"],
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
                    "owner": "hydrius",
                    "population": 100,
                    "RRE"       : 3,
                    "Water"     : 3,
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

        screen.refresh()

curses.endwin()









