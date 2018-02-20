# flask-blueprint/blue/api/routes.py
# importing blueprint from flask

from flask import Blueprint, jsonify
import sys
import os
# intantiate the blueprint
# mod is the name
# blueprint taking two arguments
# first is the app folder and the __name__
mod = Blueprint('api', __name__)


# This we use a decorator to initialize the routes and in the paramenter we get the routes details
# in this case it's /getStuff
# this is how we going to acces it. http://127.0.0.1:5000/api/getStuff, we have api in this url because
# we define in the run.py that the url_prefix is /api we want get anything from the api if we don't specified.

@mod.route('/getStuff')

# This is the function that what we are going to show a json ouput on the api.
def getStuff():
    platform = sys.platform
    load = os.getloadavg()
    User = os.environ['USER']
    return jsonify({
        'User' : User,
        'Plaform': platform,
        'actual_load': load,
        })
