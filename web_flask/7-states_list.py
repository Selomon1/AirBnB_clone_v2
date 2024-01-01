#!/usr/bin/python3
"""
Script to start a Flask web application that displays a list of States
"""
from models import storage
from models.state import State
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/state_list', strict_slashes=False)
def states_list():
    """
    Route that display a list of all state objects sorted by name.
    """
    states = storage.all("State").values()
    sorted_states = sorted(states, key=lambda state: state.name)

    return render_template('7-states_list.html', states=sorted_states)


@app.teardown_appcontext
def teardown(exc):
    """
    Teardown method to remove the current SQLAlchemy Session.
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
