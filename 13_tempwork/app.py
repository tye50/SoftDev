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

print(header)
# -------------------------------------------------------

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/wdywtbwygp")
def banana():
    return render_template("tablified.html", j = jobs, p = percents, h = header)
    
if __name__ == "__main__":
        app.debug = True
        app.run()
