# program that outputs a random number between 1 and 10

import random

x = int(input("Enter range value 1:"))
y = int(input("Enter range value 2:"))

number = random.randint(x,y)

print("Random number = ", number)