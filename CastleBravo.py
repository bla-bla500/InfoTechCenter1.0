print("\n**********************************\n")

print("Gasoline Branch\n")

import random
from time import sleep

#Why have functions when we only need to call them once
#they can be made into functions again at any time if needed
#And the last function needs the other two to work so why not make one bigger function
#making this a function is also questionable but may be best depending on how we will use it
def gasLevelAlert():
    listOfGasStations = ["Shell", "VP", "Meijer", "Sams Club", "Marathon", "Speedway", "Circle K"]
    gasLevelList = ["Empty", "Almost empty", "Quarter full", "Half Full", "Three Quarters Full", "Almost full", "Full"]
    gasStation = random.choice(listOfGasStations)
    x = random.randint(0, len(gasLevelList)-1)
    gasLevel = gasLevelList[x]
    milesToGasStation = round(random.uniform(1+(25*(x-1)),25+(25*(x-1))),1)
    if gasLevel == "Empty":
        print("Warning you are on empty")
        sleep(2)
        print("Calling Triple AAA")
    elif gasLevel != "Full":
        print(f"You gas tank is {gasLevel}")
        if x <= 2: #change number to change how low tank has to be to show distance to nearest gas station
            print(f"Nearest gas station is {gasStation}, it is {milesToGasStation} miles away")
    else:
        print("Refilled")

gasLevelAlert()
