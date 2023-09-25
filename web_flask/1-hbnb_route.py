#!/usr/bin/python3
"""this script display Hello HBNB!"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    '''
    this script that starts a Flask web application:
    '''
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    '''this display HBNB'''
    return "HBNB"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
