print("\n***************************************\n")

print("Weather Branch\n")

#import libraries here

import random
from time import sleep



def weather():
    weatherForcast = ["sunny", "raining", "cloudy", "snowing", "icy", "windy"]
    return weatherForcast[random.randint(0,len(weatherForcast)-1)] #overly complicated way of doing random.choice but I made it so it's staying


print (weather())