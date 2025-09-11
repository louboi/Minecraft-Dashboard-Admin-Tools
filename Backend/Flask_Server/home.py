from flask import Flask, render_template # type: ignore
import os

app = Flask(__name__)

# Routing for the Homepage for the server
@app.route("/")
def index():
    return render_template('index.html')

# Routing for the user management page
@app.route('/user/<Username>')
def manage_user(Username=None):
    return render_template('Userpage.html', uname=Username)

# Routing for each of the command actions
@app.route('/user/<name>/ban')
def ban(name=None):
    command = str('python RCON_Connector.py 1 ' + str(name))
    os.system(command)
    return name + ' has been banned', 204

@app.route('/user/<name>/pardon')
def pardon(name=None):
    command = str('python RCON_Connector.py 10 ' + str(name))
    os.system(command)
    return name + ' has been pardoned', 204

@app.route('/user/<name>/op')
def op(name=None):
    command = str('python RCON_Connector.py 3 ' + str(name))
    os.system(command)
    return name + ' is now an operator', 204

@app.route('/user/<name>/deop')
def deop(name=None):
    command = str('python RCON_Connector.py 4 ' + str(name))
    os.system(command)
    return name + ' is no longer an operator', 204

@app.route('/user/<name>/kick')
def kick(name=None):
    command = str('python RCON_Connector.py 8 ' + str(name))
    os.system(command)
    return name + ' has been kicked', 204

@app.route('/user/<name>/kill')
def kill(name=None):
    command = str('python RCON_Connector.py 9 ' + str(name))
    os.system(command)
    return name + ' has been dispatched of', 204