'''
Tracy Ye
Loonch
SoftDev
K06 -- Divine Your Destiny! Learning how to parse CSV files.
2024-09-19
Time Spent :
'''

import csv

with open("occupations.csv", newline='') as file:
    r = csv.DictReader(file)
    for row in r:
        print(row['Job Class'], row['Percentage'])
    
print(row)
    
    