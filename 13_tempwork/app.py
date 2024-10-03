'''
Tracy Ye
JST
SoftDev
K13 -- Template for Success: Ultimate compilation of everything we have done and learned so far
2024-10-02
Time Spent : 
'''

import csv, random
jobs = []
percents = []
header = []

with open ("data/occupations.csv", newline='') as csvfile:
    file = csv.DictReader(csvfile)
    for i in file:
        jobs.append(i["Job Class"])
        percents.append((float)(i["Percentage"]))
    header = list(i.keys())
        
jobs = jobs[:len(jobs)-1]
percents = percents[:len(percents)-1]

title = "Weighted Jobs in Room 250"
roster = ["Tracy Ye", "Jessica Yu", "Stella Yampolsky"]

def randWeighted():
    return random.choices(jobs, weights = percents) # (sequence, weight, num returns)
# -------------------------------------------------------

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def main():
    return "<center>"+"<br>"*15+"<a href= 'http://127.0.0.1:5000/wdywtbwygp'>Click! Here!</a></center>"
    
@app.route("/wdywtbwygp")
def banana():
    return render_template("tablified.html", j = jobs, p = percents, h = header, t = title, r = roster, randW = randWeighted())
    
if __name__ == "__main__":
        app.debug = True
        app.run()
