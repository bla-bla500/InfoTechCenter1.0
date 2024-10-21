print("\n**********************************\n")

print("Gasoline Branch\n")

import random
from time import sleep


#Why have two functions when we only need to call them once
#I optimized it because of that
def gasLevelAlert():
    listOfGasStations = ["Shell", "VP", "Meijer", "Sams Club", "Marathon", "Speedway", "Circle K"]
    gasLevelList = ["Empty", "Low", "Quarter Tank", "Half Tank", "Three Quarter Tank", "Almost full", "Full"]
    gasLevel = random.choice(gasLevelList)
    gasStation = random.choice(listOfGasStations)
    