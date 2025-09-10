from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/user/<name>/ban')
def ban(name=None):
    command = str('python RCON_Connector.py 1 ' + str(name))
    os.system(command)
    return name + ' has been banned', 204

@app.route('/user/<Username>')
def manage_user(Username=None):
    return render_template('Userpage.html', uname=Username)