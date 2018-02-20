# flash-blueprint/blue/__init__.py
from flask import Flask

app = Flask(__name__)

from blue.api.routes import mod
from blue.sites.routes import mod

app.register_blueprint(sites.routes.mod)
app.register_blueprint(api.routes.mod, url_prefix='/api')