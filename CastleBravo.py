print("\n***************************************\n")

print("Weather Branch\n")

#import libraries here

import random  # importing random to choose weather conditions
from time import sleep  # importing sleep to add a delay for realistic timing



def weather():
    weatherForcast = ["sunny", "rainy", "cloudy", "snowy", "icy", "windy"]
    return weatherForcast[random.randint(0, len(weatherForcast) - 1)]  # overly complicated way of doing random.choice but I made it so it's staying

# Get a random weather alert from the weather() function
weatherAlert = weather()

# Define the VRS (Vehicle Regulation System) function
def VRS():
    if weatherAlert == "snowy":
        speedLimit = "55"
        alarmTime = "30"  # extra time needed in snowy weather
    elif weatherAlert == "icy":
        speedLimit = "40"
        alarmTime = "15"  # less time needed but slower speed due to icy roads
    elif weatherAlert == "rainy":
        speedLimit = "70"
        alarmTime = "40"  # rainy but manageable, more alarm time
    elif weatherAlert == "windy":
        speedLimit = "80"
        alarmTime = "45"  # windy conditions require slower speeds

    # If the weather is bad, adjust alarm and speed limits accordingly
    if weatherAlert == "snowy" or weatherAlert == "icy" or weatherAlert == "windy" or weatherAlert == "rainy":
        print("The national Weather Service has updated our alarm by " + alarmTime + " minutes because of the forecast of " + weatherAlert + " weather conditions.")
        sleep(1)  # adding delay to simulate processing time
        print("VRS system has been engaged only allowing you to drive " + speedLimit + " mph")
    # For cloudy weather, there is no need to engage VRS
    elif weatherAlert == "cloudy":
        print("The NRS is predicting " + weatherAlert + " weather conditions. Drive safe.")
    # If it's sunny, the VRS system will not engage
    else:
        print("VRS system has been disengaged")

# Call the VRS function to simulate the system response
VRS()
