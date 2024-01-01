#!/usr/bin/python3
"""
Script that starts a Flask web application with several routes
"""
from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    return 'Hello HBNB!'


@app.route('/hbnb')
def display_hbnb():
    return 'HBNB'


@app.route('/c/<text>')
def display_c_text(text):
    return 'C ' + text.replace('_', ' ')


@app.route('/python/')
@app.route('/python/<text>')
def display_python_text(text='is cool'):
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>')
def display_number(n):
    return f'{n} is a number'


@app.route('/number_template/<int:n>')
def display_number_template(n):
    return render_template('6-number_odd_or_even.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def odd_or_even(n):
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
