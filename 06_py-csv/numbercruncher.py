'''
Tracy Ye
Loonch
SoftDev
K06 -- Divine Your Destiny! Learning how to parse CSV files.
2024-09-19
Time Spent : 2 hours
'''

import csv, random

with open("occupations.csv", newline='') as file:
    r = csv.DictReader(file)
    

    random = random.randint(0, 998) # pick random between 0 and total x10
    num = 0 # add on percent x10 each row, if > rand then return job
    
    for row in r:
        # print(row['Job Class'], row['Percentage']) dictreader creates a dictionary of dictionaries (?)
        values = list(row.values()) # list containing job[0], percent[1]
        num += float(values[1])*10
        if (num >= random):
            print(values[0])
            break
