'''
Tracy Ye
JST
SoftDev
K18 -- Serving Looks : Websites with static
2024-10-17
Time Spent :
'''

from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
def home():
    return ipsum()

@app.route("/static/index.html")
def ipsum():
    return render_template("index.html")

if __name__ == "__main__":
    app.debug = True
    app.run()