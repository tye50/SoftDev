import math, random

def createPlane(r, c):
    return [[0]*c]*r

for i in createPlane(32, 4):
    print(i)

def createSchedule():
    return [[createPlane(32, 4), random.randint(1, 24)]*2]
