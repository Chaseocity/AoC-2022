#Advent of Code 2022
#Day 9: Rope Bridge
#Part 2

import os
import sys

#Declare variables
ropePos = []

#Set initial conditions of rope sections
for i in range(10):
    sectionPos = ["0,0"]
    ropePos.append(sectionPos)

#Open input file
with open(os.path.join(sys.path[0], "d9input.txt"), 'r') as inputFile:
    #Read lines from input file
    for line in inputFile:
        #Get direction and distance
        direction = line[0]
        distance = int(line [2:-1])
        #Loop based on distance
        for _ in range(distance):
            #Get H position
            hx = int(ropePos[0][-1].split(",")[0])
            hy = int(ropePos[0][-1].split(",")[1])            
            #Update H position 
            if direction == "L":
                hx -= 1
            if direction == "R":
                hx += 1
            if direction == "U":
                hy += 1
            if direction == "D":
                hy -= 1
            #Add position to array
            ropePos[0].append(str(hx) + "," + str(hy))

            #Update section positions
            for i in range(1,10):
                #Get section positions
                x1 = int(ropePos[i][-1].split(",")[0])
                y1 = int(ropePos[i][-1].split(",")[1])
                x2 = int(ropePos[i-1][-1].split(",")[0])
                y2 = int(ropePos[i-1][-1].split(",")[1])
                #Update section positions
                #Diagonal move
                if x1 > x2 + 1 and y1 > y2 + 1:
                    x1 -= 1
                    y1 -= 1
                if x1 < x2 - 1 and y1 > y2 + 1:
                    x1 += 1
                    y1 -= 1
                if x1 > x2 + 1 and y1 < y2 - 1:
                    x1 -= 1
                    y1 += 1
                if x1 < x2 - 1 and y1 < y2 - 1:
                    x1 += 1
                    y1 += 1
                #Straight move
                if x1 > x2 + 1:
                    x1 -= 1
                    #Check diagonal
                    if y1 != y2:
                        y1 = y2
                if x1 < x2 - 1:
                    x1 += 1
                    #Check diagonal
                    if y1 != y2:
                        y1 = y2
                if y1 > y2 + 1:
                    y1 -= 1
                    #Check diagonal
                    if x1 != x2:
                        x1 = x2
                if y1 < y2 - 1:
                    y1 += 1
                    #Check diagonal
                    if x1 != x2:
                        x1 = x2
                #Add section position to array
                ropePos[i].append(str(x1) + "," + str(y1))

    
    #Convert array to set to get unique values
    visitedPos = set(ropePos[9])
    
#Output count of visited positions for end of rope
print(len(visitedPos))

#Close input file
inputFile.close()