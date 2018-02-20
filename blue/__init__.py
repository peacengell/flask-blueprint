# flash-blueprint/blue/__init__.py
# import Flask
from flask import Flask
# initialiase the flask instance
app = Flask(__name__)

# import api and sites from the blue folder.
from blue.api.routes import mod
from blue.sites.routes import mod

# Register the api and sites app by calling
# register_blueprint on the routes.
app.register_blueprint(sites.routes.mod)
app.register_blueprint(api.routes.mod, url_prefix='/api')