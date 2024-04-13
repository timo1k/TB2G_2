from flask import Flask, redirect, url_for, request
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route('/success/<user>/<passw>')
def success(user, passw):
   # answer = getGPT("smurf4934@gmail.com","123456!")
   answer = 1#getGPT(user, passw)
   return '%s' % (answer)


@app.route('/error')
def error():
   return 'error'

if __name__ == '__main__':
   app.run(debug=True, port=8080)
