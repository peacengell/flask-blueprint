# flask-blueprint/blue/api/routes.py
from flask import Blueprint

mod = Blueprint('api', __name__)

@mod.route('/getStuff')

def getStuff():
    return '{"result" : "Ypu are in the API!!!}'