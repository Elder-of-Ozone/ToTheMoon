from console import Console
from testData import Test_DATA
import copy, json

from logic import logic
"""

Just a place to test new features.




"""
Test_DATA = Test_DATA()

user = Test_DATA.user
easy = Test_DATA.easy


planets = Test_DATA.generatePlanets()
fleets = Test_DATA.fleets

user["planets"] = [copy.deepcopy(planets[0]), copy.deepcopy(planets[1])]
easy["planets"] = [copy.deepcopy(planets[2])]

user["fleets"] =[copy.deepcopy(fleets["fleet2"]), copy.deepcopy(fleets["fleet1"])]

user["fleets"][0]["origin"] = copy.deepcopy(planets[0])
user["fleets"][1]["origin"] = copy.deepcopy(planets[1])

user["planets"][0]["fleets"] = copy.deepcopy(user["fleets"][0])
user["planets"][0]["fleets"] = copy.deepcopy(user["fleets"][0])

#print planets[3]
logic.planets.new(user, planets[3], user["fleets"][0])
print user["fleets"]
        
#console = Console(user, planets, fleets)


# Moving fleet1 @ p1 to p2

#message = "MOVE"
#console.move(user["fleets"][0], user["planets"][1], user["planets"][0])
 
#for i in range(1,6):
#    console.updateQueue()








