#Advent of Code 2022
#Day 7: No Space Left On Device
#Part 1

import os
import sys
from lxml import etree
#Declare variables
root = etree.Element("root")
parentFolder = root
rootFolderSize = 0
folderSize = 0
smallestFolder = 100000000
diskSpace = 70000000
requiredSpace = 30000000

#Open input file
with open(os.path.join(sys.path[0], "d7input.txt"), 'r') as inputFile:
    #Read lines from input file
    for line in inputFile:
        #Check if user command
        if line[0] == "$":
            #Trim command
            command = line[2:-1]

            # Set parent folder if cd command
            if command[:2] == "cd":
                #Back up one level
                if command[3:] == "..":
                    parentFolder = parentFolder.getparent()
                #Set parent folder if not root
                elif command[3:] != "/":
                    parentFolder = parentFolder.find(command[3:])                  
        #Create folder node if folder is listed
        elif line[:3] == "dir":
            etree.SubElement(parentFolder, line[4:-1])
        #Add file node
        else:
            #Get file information
            fileSize = line.split(" ")[0]
            fileName = line.split(" ")[1][:-1]
            #Add attribute from file information
            etree.SubElement(parentFolder, fileName, size=fileSize)

#Find total used space
for i in root.iterdescendants():
    if i.get("size") != None:
        #Add file size to total
        rootFolderSize += int(str(i.get("size")))

#Calcualte unused space
freeSpace = diskSpace - rootFolderSize

#Find all folders with total sizes under limit
for i in root.iterdescendants():
    #Iterate through all descendants of folder
    for j in i.iterdescendants():
        if j.get("size") != None:
            #Add file size to total
            folderSize += int(str(j.get("size")))
    #Check total folder size
    if folderSize + freeSpace >= requiredSpace and folderSize < smallestFolder:
        smallestFolder = folderSize
    #Reset folder size
    folderSize = 0

#Output smallest folder within limits
print(smallestFolder)

#Close input file
inputFile.close()
