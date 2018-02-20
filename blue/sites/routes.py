# flask-blueprint/blue/sites/routes.py
# import blueprint from flask.
from flask import Blueprint

# intantiate the blueprint
# mod is the name
# blueprint taking two arguments
# first is the app folder and the __name__
mod = Blueprint('site', __name__)

# This we use a decorator to initialize the routes and in the paramenter we get the routes details
# in this case it's /homepage
# this is how we going to acces it. http://127.0.0.1:5000/homepage
@mod.route('/homepage')

# This is the function that what we are going to show on the site.
def homepage():
    return '<h1> You are on the home page!!!</h1>'