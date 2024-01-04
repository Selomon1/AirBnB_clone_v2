#!/usr/bin/python3
"""
Script of Flask web application that display a list of States and their cities
"""
from flask import Flask, render_template
from models import *
from models import storage

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """
    Route that display list of states and their cities
    """
    states = storage.all("State").values()
    sorted_states = sorted(states, key=lambda state: state.name)

    return render_template('8-cities_by_states.html', states=sorted_states)


@app.teardown_appcontext
def teardown(exception):
    """
    Remove the current SQLAlchemy session
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
