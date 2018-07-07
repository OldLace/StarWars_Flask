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

# @app.route('/ten', methods = ['GET', 'POST'])
# def ten():
#     req = requests.get(url="https://pokeapi.co/api/v2/pokemon-form/")


# @app.route('/pokemon/<num>', methods = ['GET','POST'])
# def pokemon(num):
#     lst = []
#     for i in range(1,55):
#         lst.append(i)
#     num = i        
#     req = request.get(url="https://pokeapi.co/api/v2/pokemon-form/")
#     creature = req.json()
#     name = creature['name']
#     return "<h2>Profile for {{name}}</h2>"

# @app.route('/second')
# def second():
#     if request.method == 'POST':
#         name = request.form['name']
#         fightstyle = request.form['fightstyle']
#         return render_template('/second.html',fightstyle=fightstyle)
