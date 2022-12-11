#Advent of Code 2022
#Day 8: Treetop Tree House
#Part 1

import os
import sys

#Declare variables
treeMap = []
visibleTrees = 0
edgeVisible = False
leftVisible = True
rightVisible = True
topVisible = True
bottomVisible = True

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
            #Check for grid edge
            if x == 0 or x == len(treeMap[y])-1 or y == 0 or y == len(treeMap)-1:
                edgeVisible = True
            #Check for left visibility
            for i in range(0,x):
                if treeMap[y][i] >= tree:
                    leftVisible = False
            #Check for right visibility
            for i in range(x+1,len(treeMap[y])):
                if treeMap[y][i] >= tree:
                    rightVisible = False
            #Check for top visibility
            for i in range(0,y):
                if treeMap[i][x] >= tree:
                    topVisible = False
            #Check for bottom visibility
            for i in range(y+1,len(treeMap)):
                if treeMap[i][x] >= tree:
                    bottomVisible = False

            #Add to count if visible
            if edgeVisible or leftVisible or rightVisible or topVisible or bottomVisible:
                visibleTrees += 1

            #Reset variables
            edgeVisible = False
            leftVisible = True
            rightVisible = True
            topVisible = True
            bottomVisible = True

#Output visible tree count
print(visibleTrees)

#Close input file
inputFile.close()