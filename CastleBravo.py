print("\n***************************************\n")
print("Weather Branch\n")

# Import libraries here
import random  # Importing random to choose weather conditions
from time import sleep  # Importing sleep to add a delay for realistic timing

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
        print(f"The national Weather Service has updated our alarm by {alarmTime} minutes because of the forecast of {weatherAlert} weather conditions.")
        sleep(1)  # Adding delay to simulate processing time
        print(f"VRS system has been engaged, only allowing you to drive {speedLimit} mph.")
    # For cloudy weather, provide a safe driving message
    elif weatherAlert == "cloudy":
        print(f"The NRS is predicting {weatherAlert} weather conditions. Drive safe.")
    # If it's sunny, the VRS system will not engage
    else:
        print("VRS system has been disengaged")

# Call the VRS function to simulate the system response
VRS()