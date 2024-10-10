# Tracy Ye
# SoftDev
# Oct 09, 2024

from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission

app = Flask(__name__)    #create Flask object

@app.route("/")
def disp_loginpage():
    return render_template( 'login.html' )


@app.route("/resp", methods=['GET', 'POST'])
def response():
    if request.method == "GET":
        return render_template("responses.html", r = request.args['username'], method = request.method) #response to a form submission
    if request.method == "POST":
        return render_template("responses.html", r = request.form['username'], method = request.method) #response to a form submission
    
if __name__ == "__main__": 
    app.debug = True 
    app.run()
