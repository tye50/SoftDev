# Tracy Ye
# SoftDev
# September 23, 2024

from flask import Flask
app = Flask(__name__)                 #create instance of class Flask

@app.route("/")                       #assign fxn to route
def hello_world():
    print("about to print __name__...")
    print(__name__)                   #where will this go?
    return "No hablo queso!"

app.debug = True

app.run()

'''
I had no clue what debugger did, so I searched it up. Debugger apparently
makes it harder for attackers to access and change your code via flask?
And you can access it using /console, but I don't know where to write the
(didn't do anything in the terminal).
'''