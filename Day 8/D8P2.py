#Advent of Code 2022
#Day 8: Treetop Tree House
#Part 2

import os
import sys

#Declare variables
treeMap = []
leftView = 0
rightView = 0
topView = 0
bottomView = 0
maxScenicScore = 0

#Open input file
with open(os.path.join(sys.path[0], "d8input.txt"), 'r') as inputFile:
    #Read lines from input file
    for line in inputFile:
        #Add characters in line to row
        row = []
        for height in line[:-1]:
            row.append(int(height))
        #Add row to matrix
        treeMap.append(row)

    #Iterate through all trees in map
    for y in range(0,len(treeMap)):
        for x in range(0,len(treeMap[y])):
            #Set current tree
            tree = treeMap[y][x]
            #Check left visibility
            while True:
                for i in range(0,x):  
                    leftView += 1             
                    if treeMap[y][x-1-i] >= tree:
                        break
                break
            #Check right visibility
            while True:
                for i in range(x+1,len(treeMap[y])):
                    rightView += 1
                    if treeMap[y][i] >= tree:
                        break
                break
            #Check top visibility
            while True:
                for i in range(0,y):
                    topView += 1
                    if treeMap[y-1-i][x] >= tree:
                        break
                break
            #Check bottom visibility
            while True:
                for i in range(y+1,len(treeMap)):
                    bottomView += 1
                    if treeMap[i][x] >= tree:
                        break
                break

            #Calculate scenic score
            scenicScore = leftView * rightView * topView * bottomView

            #Find max scenic score
            if scenicScore > maxScenicScore:
                maxScenicScore = scenicScore

            #Reset variables
            leftView = 0
            rightView = 0
            topView = 0
            bottomView = 0
            
#Output visible tree count
print(maxScenicScore)

#Close input file
inputFile.close()