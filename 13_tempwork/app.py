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
with open ("data/occupations.csv", newline='') as csvfile:
    file = csv.DictReader(csvfile)
    for i in file:
        jobs.append(i["Job Class"])
        percents.append((float)(i["Percentage"]))
        
jobs = jobs[:len(jobs)-1]
percents = percents[:len(percents)-1]

print(percents)
# -------------------------------------------------------

# from flask import Flask, render_template
# app = Flask(_name_)
# 
# @app.route("/wdywtbwygp")
# def banana():
#    
# if _name_ == "_main_":
#     app.debug = True
#     app.run()
