#Advent of Code 2022
#Day 9: Rope Bridge
#Part 1

import os
import sys

#Declare variables
tPos = ["0,0"]
hx = 0
hy = 0
tx = 0
ty = 0

#Open input file
with open(os.path.join(sys.path[0], "d9input.txt"), 'r') as inputFile:
    #Read lines from input file
    for line in inputFile:
        #Get direction and distance
        direction = line[0]
        distance = int(line [2:-1])
        #Loop based on distance
        for _ in range(distance):            
            #Update H position 
            if direction == "L":
                hx -= 1
            if direction == "R":
                hx += 1
            if direction == "U":
                hy += 1
            if direction == "D":
                hy -= 1
            #Update T position
            if tx > hx + 1:
                tx -= 1
                #Check diagonal
                if ty != hy:
                    ty = hy
            if tx < hx - 1:
                tx += 1
                #Check diagonal
                if ty != hy:
                    ty = hy
            if ty > hy + 1:
                ty -= 1
                #Check diagonal
                if tx != hx:
                    tx = hx
            if ty < hy - 1:
                ty += 1
                #Check diagonal
                if tx != hx:
                    tx = hx
            #Save T position
            tPos.append(str(tx) + "," + str(ty))

    
    #Convert array to set to get unique values
    visitedPos = set(tPos)
    
#Output count of visited positions
print(len(visitedPos))

#Close input file
inputFile.close()