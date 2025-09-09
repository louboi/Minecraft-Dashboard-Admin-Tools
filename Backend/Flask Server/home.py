from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    os.system('python RCON_Connector.py 1 ImperialFir6997')
    return 'Good', 204