from flask import Flask, render_template, request
# create an app and give it a name
app = Flask('star_wars') #that string is the name of the folder
# from the current directory, import views
from . import views
# views is where all your code is
 