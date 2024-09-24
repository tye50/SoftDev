# Tracy Ye
# SoftDev
# September 23, 2024

from flask import Flask
app = Flask(__name__)             #create instance of class Flask

@app.route("/")                   #assign fxn to route
def hello_world():
    print("about to print __name__...")
    print(__name__)               #where will this go?
    return "No hablo queso!"

app.run()

'''
print prints to the terminal. I predict it will print "about to print __name__... (website link)"
'''

'''
when I opened it in the terminal, it didn't immediately print the message.
however, when i opened and then closed the website, and then closed crt+c
the flask application, it printed the "about to print" message.
'''