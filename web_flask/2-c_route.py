#!/usr/bin/python3
"""
Script that starts a Flask web application with three routes
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hell0_hbnb():
    """ Display 'Hello HBNB!' """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """ Display 'HBNB' """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def display_c_tex(text):
    """ Display 'C' followed by the value of the text variable """
    return 'C {}'.format(text.replace('_', ' '))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
