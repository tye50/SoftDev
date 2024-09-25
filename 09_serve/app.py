'''
Tracy Ye
NewMixUpGroup
SoftDev
K09 -- Putting it Together : Learning about Flask and app.py
2024-09-24
Time spent: 
'''

import random
import csv

occupation_list = []
percentages = []

with open('occupations.csv', newline ='') as csvfile:
    file = csv.DictReader(csvfile)
    for row in file:
        occupation_list.append(row['Job Class']) # fill list with occupations
        percentages.append((float)(row['Percentage'])) # fill list with casted percents

occupation_list = occupation_list[1:-1] # remove the first and last
percentages = percentages[1:-1] # remove the first and last

def select_occupation(occupation_list, percentages):
    return random.choices(occupation_list, weights=percentages, k=1) # using the built in weighted random, return a random occupation
    
def ret(): # return using html syntax
    ret = "TNPG = thisNewGroup<br>Roster = Tracy?<br><br><h1>" + str(select_occupation(occupation_list, percentages)) + "</h1><br><br>"+ str(occupation_list)
    return ret
    
    # -------------------------------------------------------------
    
from flask import Flask
app = Flask(__name__)

@app.route("/")
def randOccupation():
    print(__name__)
    return ret() # calling the function defined above

app.run(port=5001) # We were having trouble in class with port 5000 already being used, so we specified the port