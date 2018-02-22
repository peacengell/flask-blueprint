# flask-blueprint/blue/api/routes.py
# importing blueprint from flask

from flask import Blueprint, jsonify
import sys
import os
import time
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
    pids = []
    for subdir in os.listdir('/proc'):
        if subdir.isdigit():
            pids.append(subdir)


    platform = sys.platform
    load = os.getloadavg()
    User = os.environ['USER']
    cpu = os.cpu_count()
    today_date = time.strftime(("%y-%m-%d"))
    today_time = today = time.strftime(("%H:%M"))


    return jsonify({
        'Cpu': cpu,
        'User' : User,
        'Plaform': platform,
        'Actual_load': load,
        'Total Running process': len(pids),
        "Today's Date" : today_date,
        "Today's Time" : today_time
        })
