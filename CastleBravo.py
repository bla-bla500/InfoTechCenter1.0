import sys
import time    # Make sure to import necessary libraries

#colors
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
RESET = "\033[0m"

print("\nWelcome to InfoTecCenter V1.0\n")

"""
#version I like better (not tested for a while)

x = 0
while x < 100:
    x += 1
    message = ("Loading", str(x) + '%' + YELLOW)
    time.sleep(0.2)
    sys.stdout.write("\r" + str(message))
    if x == 100:
        print(GREEN + "\rLoaded" + RESET)
"""

#Stuff you want

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