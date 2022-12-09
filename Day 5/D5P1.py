#Advent of Code 2022
#Day 5: Supply Stacks
#Part 1

import os
import sys

#Declare variables
totalContains = 0
cratesInput = []
crates = []
crateColumn = ""
topCrates = ""

#Open input file
with open(os.path.join(sys.path[0], "d5input.txt"), 'r') as inputFile:
    
    #Read lines from input file
    for i, line in enumerate(inputFile):
        #Store crate arrangement in array
        if i < 8:
            cratesInput.append(line[:-1])
        
        #Organize crate arrangement into strings (run once)
        if i == 9:
            #Split each column into a string
            for x in range(9):
                for y in range(8):
                    crate = str(cratesInput[y])[4*x:4*x+4]

                    #Check if crate exists in selected location
                    if crate[1] != " ":
                        #Add it to the column string
                        crateColumn = crate[1] + crateColumn

                #Add column stack to arrangement array
                crates.append(crateColumn)

                #Clear column stack
                crateColumn = ""

        #Execute moves in remaining lines
        if i > 9:
            #Split move, from, and to column numbers
            moveSplit = line[:-1].split(" ")
            moveNum = int(moveSplit[1])
            fromNum = int(moveSplit[3])
            toNum = int(moveSplit[5])

            #Edit column strings according to move
            for z in range(moveNum):
                #Get crate to be moved
                movedCrate = crates[fromNum-1][-1]

                #Remove crate from column
                crates[fromNum-1] = crates[fromNum-1][:-1]

                #Add crate to column
                crates[toNum-1] += movedCrate

    #Get top crate of each column
    for x in range(9):
        topCrates += crates[x][-1]
    print(topCrates)

#Close input file
inputFile.close()