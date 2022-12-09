#Advent of Code 2022
#Day 6: Tuning Trouble
#Part 1

import os
import sys

#Declare variables
totalContains = 0
index = 4

#Open input file
with open(os.path.join(sys.path[0], "d6input.txt"), 'r') as inputFile:
    
    #Read first four characters
    buffer = inputFile.read(index)

    #Loop through remaining characters from input file
    while True:
        #Store next character
        nextChar = inputFile.read(1)
        index += 1

        #Exit loop if at file end
        if not nextChar:
            break

        #Remove leading char and add next char
        buffer = buffer[1:] + nextChar

        #Check for matches in buffer
        match = False
        for char in buffer:
            if buffer.count(char) > 1:
               match = True
        
        #Print index and buffer if no matches found
        if match == False:
            print(index)
            print(buffer)
            break

#Close input file
inputFile.close()