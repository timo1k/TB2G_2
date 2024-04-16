from flask import Flask, redirect, url_for, request
from flask_cors import CORS
from yadda import getGPT, poop
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import pickle

app = Flask(__name__)
CORS(app)

# Load pipeline and model using the binary files
model = pickle.load(open('poopie_model.pkl', 'rb'))


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
