# Tracy Ye
# SoftDev
# September 23, 2024

from flask import Flask
app = Flask(__name__)           #create instance of class Flask

@app.route("/")                 #assign fxn to route
def hello_world():
    print("the __name__ of this module is... ")
    print(__name__)
    return "No hablo queso!"

if __name__ == "__main__":      # true if this file NOT imported
    app.debug = True            # enable auto-reload upon code change
    app.run()
    
'''
I searched it up and _name_ tells the app where it is. A litte more digging
reveals that _name_ == _main_ is a conditional that makes it so if your
function is ran in anything aside from the original file it was written in,
it will skip over everything in the if statement. I think that means if I
call this hello_world() in a different file, it will not activate debugger or
run. But if I call it from v4, it will. Hoewever, everything above in the
indented "def" part will run.
'''