#Advent of Code 2022
#Day 3: Rucksack Organization
#Part 2

import os
import sys

#Declare variables
totalPriority = 0
count = 1

#Open input file
with open(os.path.join(sys.path[0], "d3input.txt"), 'r') as inputFile:
    #Read lines from input file
    for line in inputFile:
        #Store contents of first sack
        if count == 1:
            sack1 = line[:-1]
            count += 1
        #Store contents of second sack
        elif count == 2:
            sack2 = line[:-1]
            count += 1
        #Store contents of third sack and find badge
        elif count == 3:
            sack3 = line[:-1]

            #Convert to sets and compare for common item
            sack1Set = set(sack1)
            sack2Set = set(sack2)
            sack3Set = set(sack3)
            commonItemSet = sack1Set.intersection(sack2Set, sack3Set)
            commonItem = commonItemSet.pop()

            #Convert common item to priority value using ASCII value offsets
            if(ord(commonItem) <= 90):
                priority = ord(commonItem)-38
            elif(ord(commonItem) <= 122):
                priority = ord(commonItem)-96

            #Add to priority sum
            totalPriority += priority

            #Reset count
            count = 1

#Output priority sum
print(totalPriority)

#Close input file
inputFile.close()