#Advent of Code 2022
#Day 10: Cathode-Ray Tube
#Part 1

import os
import sys

#Declare variables
testCycles = [20, 60, 100, 140, 180, 220]
cycle = 1
x = 1
signalStrength = 0

#Open input file
with open(os.path.join(sys.path[0], "d10input.txt"), 'r') as inputFile:
    #Read lines from input file
    for line in inputFile:
        #Add signal strength if correct cycle count
        if cycle in testCycles:
            signalStrength += cycle * x
        #Check for add command
        if line[:3] == "add":
            #Get amount value
            addAmt = int(line.split(" ")[1][:-1])
            #Two cycles for add command
            for i in range(2):
                #Execute on second cycle
                if i == 1:
                    #Add amount to x
                    x += addAmt
                else:
                    #Update cycle count for first add cycle
                    cycle += 1
        #Update cycle count for noop cycle and second add cycle
        cycle += 1                

#Output count of visited positions
print(signalStrength)

#Close input file
inputFile.close()