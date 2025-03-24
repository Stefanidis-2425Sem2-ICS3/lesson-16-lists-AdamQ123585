# Name: Adam Qureshi
# Title: 100 Random Number Averager
# Date: Feb 20, 2024
# This Program lists 100 random numbers and then averages them

import random

Numbers = [random.randint(0,100) for i in range(100)]

print ("The 100 numbers are:")
print (Numbers)

Average = sum(Numbers)/len(Numbers)

print ("The Average of your numbers is:")
print (Average)


