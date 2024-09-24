# Tracy Ye
# SoftDev
# September 23, 2024

from flask import Flask
app = Flask(__name__)          # ...This reminds me of Java syntax

@app.route("/")                # ...This probably relates to where the link is stored?
def hello_world():
    print(__name__)            # ..."print" prints onto the terminal
    return "No hablo queso!"   # ..."return" prints onto the website

@app.route("/")   
def whatHappensNow():
    print(__name__)
    return "Pero hablo queso!"

app.run()                      # ...this runs the code

'''
the website link doesn't change even if you change the contents of the website.
'''