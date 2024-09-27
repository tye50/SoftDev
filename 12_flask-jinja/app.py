# Tracy Ye
# Untitled
# Sep 26, 2024

"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Q0:
I predict that it will make the test_temp() not work. Maybe an error will be thrown and the page won't run.
When it is run with render_template: it returns the numbers inside coll in separate rows.
When it is run without render_template: it returns a NameError stating that render_template function was not defined.

Q1:
Yes, we all say the url should look like 127.0.0.1:5000/my_foist_template

Q2:
arg1 is the file that will serve as the template
arg2 replaces the variables defined in {{}} with their cooresponding value
arg3 is the same as arg2, but with variable collection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

'''
Purple Screen of Death
a) If you try to return something that has not been defined. In this case, a function.
b) You can ignore the tracebacks that happen inside the flask package.
c) The first line with the problem found and the last line in the traceback which shows which line the error was found in.
d) No, I do not smell danger. This looks helpful.
'''

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Q0: What will happen if you remove render_template from the following statement?
# (log prediction before executing...)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "No hablo queso!"

coll = [0,1,1,2,3,5,8]

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Q1: Can all of your teammates confidently predict the URL to use to load this page?
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@app.route("/my_foist_template") 
def test_tmplt():
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Q2: What is the significance of each argument? Simplest, most concise answer best.
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    return render_template( 'model_tmplt.html', foo="fooooo", collection=coll)

@app.route("/my_scnd_template") # testing the error thing
def dos():
    return hello

if __name__ == "__main__":
    app.debug = True
    app.run()