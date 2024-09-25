'''
Tracy Ye
JST
SoftDev
K: 05 randomly selecting devos via list and parsing
2024-09-16
<Time spent: 1>
'''

import random

def randDevo():
    file = open("krewes.txt", "r") # open text file
    devos = file.read()
    
    individual = []
    individual = devos.split("@@@")
    individual = individual[1:len(individual)-1]  # remove incorrect first and last
    individual[0] = "04$$$Dua$$$Emma" # fix the incorrectly printed [0]
    individual[10] = "04$$$Naomi$$$Wiley" # fix the incorrectly printed [10]
    individual[22] = "04$$$Andy$$$Aviator-Piggy" # fix the incorrectly printed [22]
    
    period = []
    name = []
    ducky = []
    
    for i in individual: # separate into indiv lists
        temp = i.split("$$$")
        period.append(temp[0])
        name.append(temp[1])
        ducky.append(temp[2])
    
    myDict = {}
    temp = 0
    for i in name:
        myDict[i] = [period[temp], ducky[temp]]
        temp+=1
    
    randName = random.choice(name)
    ret = "Name: " + randName + ", Period: " + myDict[randName][0] + ", Ducky: " + myDict[randName][1]
    return ret

print(randDevo())