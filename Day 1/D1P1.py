#Advent of Code 2022
#Day 1: Calorie Counting
#Part 1

import os
import sys

#Declare variables
calorieCount = 0
maxCalorieCount = 0

#Open input file
with open(os.path.join(sys.path[0], "d1input.txt"), 'r') as inputFile:
    #Read lines from input file
    for line in inputFile:
        #If line isn't empty, add to calorie count
        if not line.isspace():
            calorieCount = calorieCount + int(line)
        else:
            #Check if larger than current max count. If so, update max count.
            if calorieCount > maxCalorieCount:
                maxCalorieCount = calorieCount
            #Reset count
            calorieCount = 0

#Output max count
print(maxCalorieCount)

#Close input file
inputFile.close()