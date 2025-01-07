from flask import Flask
from flask import render_template
import requests # pip install requests
import urllib.request
import urllib.parse
import json

app = Flask(__name__)

@app.route("/")
def load():
    
    data = urllib.request.urlopen("https://api.adviceslip.com/advice")
    python_ify = json.loads(data.read())
    print(python_ify)
    return render_template("main.html", x = python_ify)

if __name__ == "__main__":
    app.debug = True 
    app.run()
    
    
    
    
''' ###################################################################### '''
''' ###################################################################### '''
''' ###################################################################### '''

data = urllib.request.urlopen('https://xkcd.com/')
# print(data) # <http.client.HTTPResponse object at 0x7ff5a6504f10>
# print(data.geturl()) # returns url
# print(data.info()) # headers (web connection info?)
# print(data.read()) # source code of webpage (HTML)

req = urllib.request.Request('http://xkcd.com/')
# print(urllib.request.urlopen(req)) # same as printing the data for the url
# print(urllib.request.urlopen(req).read()) # same as reading the webpage's source

url = 'http://www.someserver.com/cgi-bin/register.cgi'
values = {'name' : 'Michael Foord',
          'location' : 'Northampton',
          'language' : 'Python' }
# data_encoded = urllib.parse.urlencode(values)
# print(data) # this returns -->   name=Michael+Foord&location=Northampton&language=Python, which is the query passed into webpages
# data_encoded = data_encoded.encode('ascii')
# print(data) # data must be in bytes -->   b'name=Michael+Foord&location=Northampton&language=Python'
# req = urllib.request.Request(url, data_encoded, method="POST")
# print(req) # the requested object is now filled in with the query data
# # print(urllib.request.urlopen(req)) # url dont exist


data = {} # populate dict
data['name'] = 'Somebody Here'
data['location'] = 'Northampton'
data['language'] = 'Python'

# url_values = urllib.parse.urlencode(data)
# url = 'http://www.example.com/example.cgi'
# full_url = url + '?' + url_values # manually piece together your url
# # data = urllib.request.urlopen(full_url) # I think this doesn't work because the domain doesn't actually take in queries

# # https://docs.python.org/3/howto/urllib2.html
# # on how to handle / work with errors

''' ###################################################################### '''

values = {'pog' : 'luca', 'eyy' : 'shu'}
# print(json.dumps(values)) # turns python dict into JSON obj string
# print(json.dumps({"c": 1, "b": 0, "a": 0}, sort_keys=True)) # can sort by keys

compact = json.dumps([1, 2, 3, {'4': 5, '6': 7}], separators=(',', ':'))
# print(compact)

pretty_print = json.dumps({'6': 7, '4': 5}, sort_keys=True, indent=2)
# print(pretty_print) # indent is how many spaces for new line
# print(json.loads(pretty_print))

x = json.loads('["foo", {"bar":["baz", null, 1.0, 2]}]')
# print(x) # turn JSON obj string back into python dict
y = json.loads('"\\"foo\\bar"')
# print(y) # ???

''' ###################################################################### '''

r = requests.get('https://api.github.com')
# print(r) # <Response[200]>
# print(r.json()) # throws error is JSON doesn't exist?

''' ###################################################################### '''
