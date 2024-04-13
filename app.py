from flask import Flask, redirect, url_for, request
from flask_cors import CORS
app = Flask(__name__)
from yadda import getGPT, poop
CORS(app)

@app.route('/startFunction')
def success():
   # answer = getGPT("smurf4934@gmail.com","123456!")
   answer = getGPT()
   return '%s' % (answer)

@app.route('/poop')
def poop():
   # answer = getGPT("smurf4934@gmail.com","123456!")
   answer = poop()
   return '%s' % (answer)


@app.route('/error')
def error():
   return 'error'

if __name__ == '__main__':
   app.run(debug=True, port=8080)
