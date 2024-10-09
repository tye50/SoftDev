# Tracy Ye
# SoftDev
# Oct 08, 2024

from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission

app = Flask(__name__)    #create Flask object

@app.route("/")
def disp_loginpage():
    return render_template( 'greetings.html' )


@app.route("/POST") # , methods=['GET', 'POST'])
def post():    return "Waaaa hooo HAAAH"  #response to a form submission


    
if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()