"""
Flask Documentation:     http://flask.pocoo.org/docs/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/

This file creates your application.
"""

import os
from flask import Flask, request

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'this_should_be_configured')


###
# Routing for your application.
###


@app.route('/api/hello_world')
def hello_world_api():
    return "Hello World"

@app.route('/api/hello_digvijay')
def hello_digvijay_api():
    return "Hello World by digvijay"

@app.route('/api/add/<num1>/<num2>')
def add_api_add(num1, num2):
    return {"result": int(num1+num2)}


###
# The functions below should be applicable to all Flask apps.
###


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=600'
    return response


if __name__ == '__main__':
    app.run(debug=True)
