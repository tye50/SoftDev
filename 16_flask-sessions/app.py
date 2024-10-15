# Tracy Ye
# SoftDev
# Oct 09, 2024

from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission
from flask import session
import os

app = Flask(__name__)    #create Flask object
app.secret_key = os.urandom(32)

@app.route("/")
def disp_loginpage():
    if 'username' in session:
        return render_template("response.html", r = session['username'], method = request.method)
    else:
        return render_template( 'login.html' )

@app.route("/resp", methods=['GET', 'POST'])
def response():
    if 'username' in session:
        # print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        # print(request.method)
        return render_template("response.html", r = session['username'], method = request.method)
    elif request.method == "GET":
        session['username'] = request.args['username']
        return render_template("response.html", r = request.args['username'], method = request.method) #response to a form submission
    elif request.method == "POST":
        session['username'] = request.form['username']
        return render_template("response.html", r = request.form['username'], method = request.method) #response to a form submission
    
@app.route("/logout", methods=['GET', 'POST'])
def logout(): 
    session.pop('username')
    return render_template("logout.html")
    
if __name__ == "__main__": 
    app.debug = True 
    app.run()
