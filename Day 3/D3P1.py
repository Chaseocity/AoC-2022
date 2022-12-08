#Advent of Code 2022
#Day 3: Rucksack Organization
#Part 1

import os
import sys

#Declare variables
totalPriority = 0

#Open input file
with open(os.path.join(sys.path[0], "d3input.txt"), 'r') as inputFile:
    #Read lines from input file
    for line in inputFile:

        #Find size of compartments by splitting string in half
        compSize = (int)(len(line) / 2)

        #Store compartment items
        comp1 = line[:compSize]
        comp2 = line[-compSize-1:]

        #Convert to sets and compare for common items
        comp1Set = set(comp1)
        comp2Set = set(comp2)
        commonItemSet = comp1Set.intersection(comp2Set)
        commonItem = commonItemSet.pop()
        
        #Convert common item to priority value using ASCII value offsets
        if(ord(commonItem) <= 90):
            priority = ord(commonItem)-38
        elif(ord(commonItem) <= 122):
            priority = ord(commonItem)-96

        #Add to priority sum
        totalPriority += priority

#Output priority sum
print(totalPriority)

#Close input file
inputFile.close()