'''
Tracy Ye
SoftDev
K23: A RESTful Journey Skyward : rest-API & NASA
2024-11-20
Time Spent :
'''

from flask import Flask
from flask import render_template
import urllib.request
import urllib.parse
import json

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
data_encoded = urllib.parse.urlencode(values)
print(data) # this returns -->   name=Michael+Foord&location=Northampton&language=Python, which is the query passed into webpages
data_encoded = data_encoded.encode('ascii')
print(data) # data must be in bytes -->   b'name=Michael+Foord&location=Northampton&language=Python'
req = urllib.request.Request(url, data_encoded, method="POST")
print(req) # the requested object is now filled in with the query data
print(urllib.request.urlopen(req)) # url dont exist


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

# app = Flask(__name__)
# 
# @app.route("/")
# def load():
#     return render_template("main.html")
# 
# 
# if __name__ == "__main__":
#     app.debug = True 
#     app.run()