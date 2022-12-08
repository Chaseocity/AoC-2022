#Advent of Code 2022
#Day 4: Camp Cleanup
#Part 1

import os
import sys

#Declare variables
totalContains = 0

#Open input file
with open(os.path.join(sys.path[0], "d4input.txt"), 'r') as inputFile:
    #Read lines from input file
    for line in inputFile:
        #Split assignments from input line
        lineSplit = line.split(",")
        range1 = lineSplit[0]
        range2 = lineSplit[1][:-1]

        #Split values from assignments
        range1Low = int(range1.split("-")[0])
        range1High = int(range1.split("-")[1])
        range2Low = int(range2.split("-")[0])
        range2High = int(range2.split("-")[1])

        #Check if one range fully contains the other
        if(range1Low <= range2Low and range1High >= range2High):
            totalContains += 1
        elif(range2Low <= range1Low and range2High >= range1High):
            totalContains += 1

#Output sum of fully contained pairs
print(totalContains)

#Close input file
inputFile.close()