#This program prints out random fruit.

import random

fruits = ('apple', 'banana', 'orange', 'pear', 'strawberry', 'avacado')

index = random.randint(0, (len(fruits)-1))

print(fruits[index])
