# Tracy Ye
# SoftDev
# September 23, 2024

from flask import Flask
app = Flask(__name__)            #create instance of class Flask

@app.route("/")                  #assign fxn to route
def hello_world():
    return "No hablo queso!"

app.run()

'''
so the app.route('/') probably links the instance "app" to the website
'''