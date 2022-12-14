#Advent of Code 2022
#Day 10: Cathode-Ray Tube
#Part 2

import os
import sys

#Declare variables
pixels = []
cycle = 1
x = 1

#Visibility check function
def checkVisible(cycle, register):
    #Get pixel position
    pixelPos = (cycle - 1) % 40
    #Check for sprite visibility
    if pixelPos >= register - 1 and pixelPos <= register + 1:
        return "#"
    else:
        return "."

#Open input file
with open(os.path.join(sys.path[0], "d10input.txt"), 'r') as inputFile:
    #Read lines from input file
    for line in inputFile:
        #Check for sprite visibility
        pixels.append(checkVisible(cycle, x))
        #Check for add command
        if line[:3] == "add":
            #Get amount value
            addAmt = int(line.split(" ")[1][:-1])
            #Two cycles for add command
            for i in range(2):
                #Execute on second cycle
                if i == 1:
                    #Check for sprite visibility
                    pixels.append(checkVisible(cycle, x))
                    #Add amount to x
                    x += addAmt
                else:
                    #Update cycle count for first add cycle
                    cycle += 1
        #Update cycle count for noop cycle and second add cycle
        cycle += 1  

#Output CRT image
for i, pixel in enumerate(pixels):
    print(pixel, end = "")
    if (i + 1) % 40 == 0:
        print(""),

#Close input file
inputFile.close()

