#Advent of Code 2022
#Day 11: Monkey in the Middle
#Part 1

import os
import sys

#Declare variables
monkeyItems = []
monkeyInspections = []
monkeyOps = []
monkeyTests = []

#Open input file
with open(os.path.join(sys.path[0], "d11input.txt"), 'r') as inputFile:
    #Read lines from input file
    for line in inputFile:
        #Check for monkey header line
        if "Monkey" in line:
            #Prepare starting items string
            itemString = inputFile.readline().split(":")[1]
            #Record starting item values
            items = []
            for i in range(len(itemString.split(","))):
                items.append(int(itemString.split(",")[i]))
            #Save starting items to matrix
            monkeyItems.append(items)

            #Initialize inspection count
            monkeyInspections.append(0)

            #Prepare operation string
            opString = inputFile.readline().split(":")[1]
            #Record operation values [operation, value as string]
            op = []
            op.append(opString.split(" ")[-2])
            op.append(opString.split(" ")[-1][:-1])
            #Save operation values to matrix
            monkeyOps.append(op)

            #Record test values [divisible by, true monkey, false monkey]
            test = []
            test.append(int(inputFile.readline().split(" ")[-1]))
            test.append(int(inputFile.readline().split(" ")[-1]))
            test.append(int(inputFile.readline().split(" ")[-1]))
            #Save test values to matrix
            monkeyTests.append(test)

#Loop through set number of rounds
for round in range(20):
    #Loop through monkeys
    for monkey in range(len(monkeyOps)):
        #Loop through monkey's items
        for item in range(len(monkeyItems[monkey])):
            #Get worry level
            worryLevel = monkeyItems[monkey][0]

            #Do operation on worry level
            #Addition
            if monkeyOps[monkey][0] == "+":
                if monkeyOps[monkey][1] == "old":
                     worryLevel = worryLevel + worryLevel
                else:
                    worryLevel = worryLevel + int(monkeyOps[monkey][1])
            #Multiplicaiton
            elif monkeyOps[monkey][0] == "*":
                if monkeyOps[monkey][1] == "old":
                     worryLevel = worryLevel * worryLevel
                else:
                    worryLevel = worryLevel * int(monkeyOps[monkey][1])

            #Increment monkey inspections
            monkeyInspections[monkey] += 1

            #Divide worry level by 3
            worryLevel = worryLevel // 3

            #Run test on current worry level and transfer item to other monkey
            if worryLevel % monkeyTests[monkey][0] == 0:
                monkeyItems[monkeyTests[monkey][1]].append(worryLevel)
            else:
                monkeyItems[monkeyTests[monkey][2]].append(worryLevel)
            #Remove item from current monkey
            monkeyItems[monkey].pop(0)

#Calcualte monkey business
#Get 2 most active monkeys
activeMonkey1 = max(monkeyInspections)
monkeyInspections.remove(activeMonkey1)
activeMonkey2 = max(monkeyInspections)
#Multiply values
monkeyBusiness = activeMonkey1 * activeMonkey2

#Output monkey business
print(monkeyBusiness)

#Close input file
inputFile.close()