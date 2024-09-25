'''
Tracy Ye
Loonch
SoftDev
K06 -- Divine Your Destiny! Learning how to parse CSV files.
2024-09-19
Time Spent : 2 hours
'''

import csv, random

occupation_list = []
percentages = []

with open("occupations.csv", newline='') as file:
    r = csv.DictReader(file)
    
    for row in r: # read the dictionary
        occupation_list.append(row['Job Class']) # fill list with occupations
        percentages.append((float)(row['Percentage'])) # fill list with casted percents

    occupation_list = occupation_list[1:-1] # remove the first and last
    percentages = percentages[1:-1] # remove the first and last

def select_occupation(occupation_list, percentages):
    return random.choices(occupation_list, weights=percentages, k=1) # using the built in weighted random, return a random occupation

print(select_occupation(occupation_list, percentages))