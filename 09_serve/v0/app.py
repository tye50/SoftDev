# Tracy Ye
# SoftDev
# September 23, 2024

from flask import Flask
app = Flask(__name__)          # ...This reminds me of Java syntax

@app.route("/")                # ..."print" prints into the terminal
def hello_world():
    print(__name__)            # ..."return" prints onto the website
    return "No hablo queso!"   # ...if i make a new definition, nothing new gets printed!

@app.route("/")   
def whatHappensNow():
    print(__name__)
    return "Pero hablo queso!"

app.run()                      # ...the website link doesn't change even if you change the contents of the website.