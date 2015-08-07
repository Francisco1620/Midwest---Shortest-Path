"""
This is a simple program that uses the A* Search Algorithm to calcuate the fastest travel route
between point A(State Capital) and point B(State Capital) in the Midwest of the United States.
"""

from queue import PriorityQueue
import random
import math
import sys


class MyPriorityQueue(PriorityQueue):
    def __init__(self):
        PriorityQueue.__init__(self)
        self.counter = 0

    def put(self, item, priority):
        PriorityQueue.put(self, (priority, self.counter, item))
        self.counter += 1

    def get(self, *args, **kwargs):
        _, _, item = PriorityQueue.get(self, *args, **kwargs)
        return item
   

def calHeuristic(currentLocation, endLocation, heuristic): #Needs to calculate heuristic for each capital to the final destination 
    currentLocation = location[currentLocation]
    endLocation = location[endLocation]
    currentLocation = currentLocation.split(",")
    endLocation = endLocation.split(",")
    x1 = float(currentLocation[0])
    x2 = float(currentLocation[1])
    y1 = float(endLocation[0])
    y2 = float(endLocation[1])
   
    heuristic = math.sqrt((x2 - x1)**2 + (y2 - y1)**2) 
     
    """
    heuristic = abs(x1 - x2) + abs(y1 - y2)
   """
    return heuristic

def aStartSearch(map, startLocation, endLocation): # A* algortithm based on pseudocode from wikipidia and my AI class 
       frontier = MyPriorityQueue()
       frontier.put(startLocation, calHeuristic(startLocation,endLocation,heuristic))
       explored = {}
       path_cost= {}
       path_cost[startLocation] = 0
       
       while not frontier.empty():
           current = frontier.get()
           
           if current == endLocation:
               break
          
           for node in map[current]:
               newCost = path_cost[current] + map[current].get(node)
               if node not in path_cost or newCost < path_cost[node]:
                   path_cost[node] = newCost
                   f_cost = newCost + calHeuristic(node, endLocation, heuristic) 
                   if node == endLocation: 
                       f_cost = 1
                       frontier.put(node, f_cost) #node becomes highest priority in the Queue
                   else:
                       frontier.put(node, f_cost)
                   explored[node] = current
       

       def shortestPath(explored, current):
        
        total_path = [current]
        while current in explored:
            current = explored[current]
            total_path.append(current)
        total_path.reverse()
        return total_path

       return shortestPath(explored, current)

#Main
MidwestLocations = ["Springfield, IL",
                    "Indianapolis, IN",
                    "Des Moines, IA",
                    "Topeka, KS",
                    "Landsing, MI",
                    "St.Paul, MN",
                    "Jefferson City, MO",
                    "Lincoln, NE",
                    "Bismarck, ND",
                    "Columbus, OH",
                    "Pierre, SD", 
                    "Madison, WI"]

location = {'Springfield, IL':'39.698333, -89.619722',
            'Indianapolis, IN':'39.791, -86.148',
            'Des Moines, IA':'41.590833, -93.620833',
            'Topeka, KS':'39.055833, -95.689444',
            'Landsing, MI':'42.733611, -84.546667',
            'St.Paul, MN':'44.944167, -93.093611',
            'Jefferson City, MO':'38.576667, -92.173611',
            'Lincoln, NE':'40.810556, -96.680278',
            'Bismarck, ND':'46.813343, -100.779004',
            'Columbus, OH':'39.983333, -82.983333',
            'Pierre, SD':'44.367966, -100.336378',
            'Madison, WI':'43.066667, -89.4'}
map = {
    'Springfield, IL': {'Indianapolis, IN':342, 'Des Moines, IA':546.6, 'Jefferson City, MO':310.3, 'Madison, WI':427.2},
    'Indianapolis, IN': {'Springfield, IL':342, 'Landsing, MI':410, 'Columbus, OH':282},
    'Columbus, OH': {'Indianapolis, IN':282, 'Landsing, MI':418.5},
    'Landsing, MI': {'Indianapolis, IN':410, 'Columbus, OH':409.4,'Madison, WI':594.3},
    'Madison, WI': {'St.Paul, MN':418.9, 'Des Moines, IA':468.0, 'Springfield, IL':425.6, 'Landsing, MI':592.7},
    'St.Paul, MN': {'Madison, WI':416.6, 'Des Moines, IA':397.7, 'Bismarck, ND':704.5, 'Pierre, SD':642.8},
    'Des Moines, IA':{'St.Paul, MN':394.6,'Madison, WI':472.0,'Springfield, IL':542.0, 'Jefferson City, MO':427.9, 'Lincoln, NE':302.8,
            'Pierre, SD':809.3},
    'Jefferson City, MO':{'Springfield, IL':310.9, 'Des Moines, IA':429.1, 'Topeka, KS':355.1,'Lincoln, NE':565.7},
    'Topeka, KS':{'Jefferson City, MO':353.9, 'Lincoln, NE':267.2},
    'Lincoln, NE':{'Topeka, KS':267.3, 'Jefferson City, MO':569.5, 'Des Moines, IA':302.6},
    'Pierre, SD':{'Lincoln, NE':730.9, 'Des Moines, IA':810.0, 'St.Paul, MN':637.6, 'Bismarck, ND':337.9},
    'Bismarck, ND':{'St.Paul, MN':703.3, 'Pierre, SD':337.4}
    }

availableLocation = ""
startLocation = ""
endLocation = ""
heuristic = 0
distant = 0
print("Hi I'm a program that can calculate the fastest route from a state captital to another state capital in the Midwest" )
print("Please pick your start location and your end location")
print("I can only calculate the routes in the MidWest of the United States")

AIresponds1 = ["The location you selected as a starting point is not in the Midwest, Please pick a location in the Midwest", 
                  "That location is not in the Midwest, Choose a location in the Midwest",
                  "Do you not know your locations in the Midwest? Choose a location in the Midwest.",
                  "Perphas you don't know your location",
                  "You can try google, since you clearly don't know the Midwest"]

AIresponds2 = ["That is not a location in the Midwest",
                  "Humans... Are you trying to waste my time?",
                  "Please don't tell me that you don't know where you want to go.",
                  "That's not part of the Midwest"#write more 
                  ]

AIresponds3 = ["You don't need me to tell you how to stay at your current location, do you? ",
                  "I will assume that your inputs were a mistake. You are human after all.",
                  "Are you trying to test me ?",
                  "Well, let me explain it to you. Your end location can't be your starting location."]

startLocation = str(input("What's your starting location? "))#User input must start with a Capital letters
for i in range(len(MidwestLocations)):#Checks to see if user input in the available list 
    if(MidwestLocations[i] == startLocation):
        availableLocation = startLocation

     
while(startLocation != availableLocation):#sidenote, keep track of how many loop and change the "AI" respondes, after ai gets "tire", it provides the user with the available locations
    if AIresponds1:# if AI is not empty
        random.shuffle(AIresponds1)
        question = AIresponds1.pop()
        print(question)
        startLocation = input("What's your starting location? ")
    else:
        sys.exit("You have wasted my time enough, good bye now!")
    for i in range(len(MidwestLocations)):
        if(MidwestLocations[i] == startLocation):
            availableLocation = startLocation

endLocation = input("Which location you would like to travel to? ")
for i in range(len(MidwestLocations)):#Checks to see if user input in the available list 
    if(MidwestLocations[i] == endLocation):
        availableLocation = endLocation

while(endLocation != availableLocation):#sidenote, keep track of how many loop and change the "AI" responds
    if AIresponds2:# if AI is not empty
        random.shuffle(AIresponds2)
        question = AIresponds2.pop()
        print(question)
        endLocation = input("Which location you would like to travel to? ")
    else:
        sys.exit("You have wasted my time enough, good bye now!")
    for i in range(len(MidwestLocations)):
        if(MidwestLocations[i] == endLocation):
            availableLocation = endLocation

while(startLocation == endLocation):#if start location an end location equal the same, pront the user to enter new locations
    if AIresponds3:# if AI is not empty
        random.shuffle(AIresponds3)
        question = AIresponds3.pop()
        print(question)
        endLocation = input("Which location you would like to travel to? ")
    else:
        sys.exit("You have wasted my time enough, good bye now!")
    for i in range(len(MidwestLocations)):
        if(MidwestLocations[i] == endLocation):
            availableLocation = endLocation

print("The fastest route is")
print(aStartSearch(map, startLocation, endLocation))



