#!/usr/bin/python3
"""
Script of Flask web application to display states
"""
from flask import Flask, render_template
from models import *
from models import storage

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def dis_states():
    """
    display list of states
    """
    states = storage.all("State").values()
    sorted_states = sorted(states, key=lambda state: state.name)
    return render_template('9-states.html', states=sorted_states)


@app.route('/states/<state_id>', strict_slashes=False)
def states_by_id(state_id):
    state = None
    states = storage.all("State").values()
    for st in states:
        if st.id == state_id:
            state = st
            break

    if state:
        cities = sorted(state.cities, key=lambda city: city.name)
        return render_template('9-states.html', state=state, cities=cities)
    return render_template('9-states.html', not_found=True)


@app.teardown_appcontext
def teardown(exception):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
