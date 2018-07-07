from . import app
from flask import render_template, request, url_for
import json
import urllib.request
import requests
import json

@app.route('/', methods = ['GET', 'POST'])
def index():
    req = requests.get(url="https://swapi.co/api/films/")
    film_json = req.json()
    film_data = film_json['results']
    empire = film_data[5]
    length = len(film_data)
    return render_template('/index.html', film_data = film_data, empire = empire, length = length)


@app.route('/trilogy', methods = ['GET', 'POST'])
def trilogy():
    return render_template('trilogy.html')

@app.route('/prequels')
def prequels():
    return render_template('prequels.html')

@app.route('/discussion', methods = ['POST'])
def forum():
    comment = request.form['comment']
    return render_template('discussion.html', comment = comment)