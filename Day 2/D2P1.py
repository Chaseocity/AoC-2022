#Advent of Code 2022
#Day 2: Rock Paper Scissors
#Part 1

import os
import sys

#Declare variables
score = 0
totalScore = 0

#Convert chars to choices
rock = ['A', 'X']
paper = ['B', 'Y']
scissors = ['C', 'Z']

#Open input file
with open(os.path.join(sys.path[0], "d2input.txt"), 'r') as inputFile:
    #Read lines from input file
    for line in inputFile:
        #Get choices from input line
        them = line[0]
        us = line[2]
        #Calculate score from choices
        if us in rock and them in rock:
            score = 4
        if us in rock and them in paper:
            score = 1
        if us in rock and them in scissors:
            score = 7
        if us in paper and them in rock:
            score = 8
        if us in paper and them in paper:
            score = 5
        if us in paper and them in scissors:
            score = 2
        if us in scissors and them in rock:
            score = 3
        if us in scissors and them in paper:
            score = 9
        if us in scissors and them in scissors:
            score = 6
        #Add score to total
        totalScore = totalScore + score

#Output max count
print(totalScore)

#Close input file
inputFile.close()