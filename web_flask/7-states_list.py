#!/usr/bin/python3
"""
Script to start a Flask web application that displays a list of States
"""
from flask import Flask, render_template
from models import storage 
from models import *

app = Flask(__name__)


@app.route('/state_list', strict_slashes=False)
def states_list():
    """
    Route that display a list of all state objects sorted by name.
    """
    states = sorted(list(storage.all("State").values()), key=lambda s: s.name)

    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown(exception):
    """
    Teardown method to remove the current SQLAlchemy Session.
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
