import sys
import time    # Make sure to import necessary libraries

#colors
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
RESET = "\033[0m"

print("\nWelcome to InfoTecCenter V1.0\n")

timeToSleep = 1 #idk why we need to make this varible, but I was told to make it
time.sleep(timeToSleep) #wait for a bit before starting system

"""
#version I like better (not tested)

x = 0
while x < 100:
    x += 1
    message = ("Loading", str(x) + '%' + YELLOW)
    time.sleep(0.2)
    sys.stdout.write("\r" + str(message))
    if x == 100:
        print(GREEN + "\rLoaded" + RESET)time.sleep(1)
"""

#Stuff you want write

x = 0  # Initialize counter for loop
ellipsis = 1  # Start ellipsis counter to control dots in the loading message

# Loop until x reaches 20
while x != 20:
    x += 1  # Increment counter on each iteration

    # Construct the loading message with an increasing number of dots
    message = ("Loading" + "." * ellipsis + YELLOW)
    ellipsis += 1  # Increase ellipsis for the next iteration

    # Overwrite the previous line in the terminal with the new message
    sys.stdout.write("\r" + str(message))

    # Introduce a small delay to simulate loading
    time.sleep(0.5)

    # Reset ellipsis count back to 1 after it reaches 3 (for a looping effect of dots)
    if ellipsis == 4:
        ellipsis = 1

    # Check if the loop has completed 20 iterations
    if x == 20:
        print(GREEN + "\rLoaded" + RESET)  # Print final message "Loaded" and overwrite the current line

time.sleep(1)
print("\n***************************************")
print("Weather Branch\n")

# Import libraries here
import random  # Importing random to choose weather conditions

# Define the weather function
def weather():
    weatherForcast = ["sunny", "rainy", "cloudy", "snowy", "icy", "windy"]
    return random.choice(weatherForcast)  # More efficient random selection

# Get a random weather alert from the weather() function
weatherAlert = weather()

# Dictionary to map weather conditions to speed limits and alarm times
weather_conditions = {
    "snowy": {"speedLimit": "55", "alarmTime": "30"},
    "icy": {"speedLimit": "40", "alarmTime": "15"},
    "rainy": {"speedLimit": "70", "alarmTime": "40"},
    "windy": {"speedLimit": "80", "alarmTime": "45"},
}

# Define the VRS (Vehicle Regulation System) function
def VRS():
    # Check if weather is one that requires a speed limit and alarm adjustment
    if weatherAlert in weather_conditions:
        speedLimit = weather_conditions[weatherAlert]["speedLimit"]
        alarmTime = weather_conditions[weatherAlert]["alarmTime"]
        print(f"\nThe national Weather Service has updated our alarm by {alarmTime} minutes because of the forecast of {weatherAlert} weather conditions.")
        time.sleep(1)  # Adding delay to simulate processing time
        print(f"\nVRS system has been engaged, only allowing you to drive {speedLimit} mph.")
    # For cloudy weather, provide a safe driving message
    elif weatherAlert == "cloudy":
        print(f"\nThe VRS is predicting {weatherAlert} weather conditions. Drive safe.")
    # If it's sunny, the VRS system will not engage
    else:
        print("\nWeather clear, VRS system has been disengaged")

# Call the VRS function to simulate the system response
VRS()

time.sleep(1)
print("\n***************************************")
print("Gasoline Branch\n")


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
        time.sleep(2)  # Pause for 2 seconds to emphasize the warning
        print("Calling Triple AAA")  # Alert for roadside assistance
    elif gasLevel != "Full":  # Check if the gas level is not full
        print(f"Your gas tank is {gasLevel}")  # Inform user of current gas level
        if x <= 2:  # Change number to change how low tank has to be to show distance to nearest gas station
            print(f"Nearest gas station is {gasStation}, it is {milesToGasStation} miles away")  # Provide nearest gas station info
    else:
        print("Refilled")  # Notify that the tank is full


gasLevelAlert()  # Call the gas level alert function
