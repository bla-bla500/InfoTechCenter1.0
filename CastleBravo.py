print("\n**********************************\n")

print("Gasoline Branch\n")

import random
from time import sleep


# Why have functions when we only need to call them once
# they can be made into functions again at any time if needed
# And the last function needs the other two to work so why not make one bigger function
# making this a function is also questionable but may be best depending on how we will use it
#this function is more scale-able than the one you made for example I could add an almost Half full tank level and it would still work
def gasLevelAlert():
    listOfGasStations = ["Shell", "VP", "Meijer", "Sams Club", "Marathon", "Speedway", "Circle K"]  # List of available gas stations
    gasLevelList = ["Empty", "Almost empty", "Quarter full", "Half Full", "Three Quarters Full", "Almost full", "Full"]  # Different levels of gas in the tank
    gasStation = random.choice(listOfGasStations)  # Randomly select a gas station
    x = random.randint(0, len(gasLevelList) - 1)  # Randomly select a gas level
    gasLevel = gasLevelList[x]
    milesToGasStation = round(random.uniform(1 + (25 * (x - 1)), 25 + (25 * (x - 1))),1)  # Calculate miles to the nearest gas station based on gas level

    if gasLevel == "Empty":  # Check if the gas level is empty
        print("Warning you are on empty")  # Alert for empty tank
        sleep(2)  # Pause for 2 seconds to emphasize the warning
        print("Calling Triple AAA")  # Alert for roadside assistance
    elif gasLevel != "Full":  # Check if the gas level is not full
        print(f"Your gas tank is {gasLevel}")  # Inform user of current gas level
        if x <= 2:  # Change number to change how low tank has to be to show distance to nearest gas station
            print(f"Nearest gas station is {gasStation}, it is {milesToGasStation} miles away")  # Provide nearest gas station info
    else:
        print("Refilled")  # Notify that the tank is full


gasLevelAlert()  # Call the gas level alert function
