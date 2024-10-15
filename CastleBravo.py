print("\n***************************************\n")

print("Weather Branch\n")

#import libraries here

import random
from time import sleep



def weather():
    weatherForcast = ["sunny", "rain7", "cloudy", "snowy", "icy", "windy"]
    return weatherForcast[random.randint(0,len(weatherForcast)-1)] #overly complicated way of doing random.choice but I made it so it's staying

weatherAlert = weather()

def VRS():
    if weatherAlert == "snowy":
        return "The national Weather Service has update out alarm by 30 minutes because of the forcast of " + weatherAlert + " weather conditions."
    else:
        return "Fine"
print(VRS())