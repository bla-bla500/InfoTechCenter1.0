import sys
import time


print("\nWelcome to InfoTecCenter V1.0\n")

"""
#a version I like better

x = 0
while x < 100:
    x += 1
    message = ("Loading", str(x) + '%')
    time.sleep(0.1)
    sys.stdout.write("\r" + str(message))
    if x == 100:
        print("\rLoaded")
"""

#Stuff you want

x = 0
ellipsis = 1
while x != 20:
    x += 1
    message = ("Loading" + "." * ellipsis)
    ellipsis += 1
    sys.stdout.write("\r" + str(message))
    time.sleep(0.1)
    if ellipsis == 4:
        ellipsis = 1
    if x == 20:
        print("\rLoaded")
