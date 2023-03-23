# __init__.py (this is the app)
from flask import Flask
app = Flask(__name__)
app.secret_key = "its a secret, keep it safe"
