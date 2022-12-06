#Advent of Code 2022
#Day 1: Calorie Counting

import os
import sys

#Declare variables
calorieCount = 0
calorieCounts = []

#Open input file
with open(os.path.join(sys.path[0], "d1input.txt"), 'r') as inputFile:
    #Read lines from input file
    for line in inputFile:
        #If line isn't empty, add to calorie count
        if not line.isspace():
            calorieCount = calorieCount + int(line)
        else:
            #Add total to counts array
            calorieCounts.append(calorieCount)
            #Reset count
            calorieCount = 0

#Sort calorie counts
sortedCounts = sorted(calorieCounts, reverse=True)

#Output top 3 counts
print(sortedCounts[:3])

#Output sum of top 3 counts
print(sum(sortedCounts[:3]))

#Close input file
inputFile.close()