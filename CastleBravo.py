
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
        print(GREEN + "\rLoaded" + RESET)
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

print("\n***************************************\n")
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
        print("\nVRS system has been disengaged")

# Call the VRS function to simulate the system response
VRS()

