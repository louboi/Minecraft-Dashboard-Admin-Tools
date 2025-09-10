from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/ban/<name>')
def ban(name=None):
    command = str('python RCON_Connector.py 1 ' + str(name))
    os.system(command)
    return 'good', 204