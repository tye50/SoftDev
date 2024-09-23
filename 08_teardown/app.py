# your heading here
'''
Tracy Ye
Loonch
SoftDev
K08 -- Learnination Via Deconstruction : Learning about virtual environments, flask, and this app.py thingy.
2024-09-20
Time spent: 25
'''

'''
DISCO:
<note any discoveries you made here... no matter how small!>

Piazza has instructions on how to create a virtual env on windows. The screen says "This is
a development server. Do not use it in a production deployment. Use a production WSGI server
instead." and links to a https website. When I open it, it says "No hablo queso!", which is
the same as typed in your hello_world() function down there. Pero hablo queso.



QCC:
0. Not sure, but working with websites gives me HTML ptsd.
1. Maybe it refers to a path like in the terminal?
2. You print to the website page? 
3. You print what is in the function you defined.
4. You are printing to the website? Because I opened the website link.
5. I'm not quite sure what this is similar to. We did work with printing to websites using python for a bit in annual computer science.
 ...

INVESTIGATIVE APPROACH:
<Your concise summary of how
 you and your team set about
 "illuminating the cave of ignorance" here...>
'''


from flask import Flask

app = Flask(__name__)                    # Q0: Where have you seen similar syntax in other langs?

@app.route("/")                          # Q1: What points of reference do you have for meaning of '/'?
def hello_world():
    print(__name__)                      # Q2: Where will this print to? Q3: What will it print?
    return "No hablo queso!"             # Q4: Will this appear anywhere? How u know?

app.run()                                # Q5: Where have you seen similar constructs in other languages?



