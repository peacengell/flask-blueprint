# flask-blueprint/run.py
# import the app from blue
# importing the app from the flask-blueprint/blue/__init__.py file where all is define and intansiates.

from blue import app
# run the app in debug mode
app.run(debug=True)