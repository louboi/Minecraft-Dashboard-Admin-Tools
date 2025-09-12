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
    return render_template('Userpage.html', uUsername=Username)

# Routing for each of the command actions
@app.route('/user/<Username>/ban')
def ban(Username=None):
    command = str('python RCON_Connector.py 1 ' + str(Username))
    os.system(command)
    return Username + ' has been banned', 204

@app.route('/user/<Username>/pardon')
def pardon(Username=None):
    command = str('python RCON_Connector.py 10 ' + str(Username))
    os.system(command)
    return Username + ' has been pardoned', 204

@app.route('/user/<Username>/op')
def op(Username=None):
    command = str('python RCON_Connector.py 3 ' + str(Username))
    os.system(command)
    return Username + ' is now an operator', 204

@app.route('/user/<Username>/deop')
def deop(Username=None):
    command = str('python RCON_Connector.py 4 ' + str(Username))
    os.system(command)
    return Username + ' is no longer an operator', 204

@app.route('/user/<Username>/kick')
def kick(Username=None):
    command = str('python RCON_Connector.py 8 ' + str(Username))
    os.system(command)
    return Username + ' has been kicked', 204

@app.route('/user/<Username>/kill')
def kill(Username=None):
    command = str('python RCON_Connector.py 9 ' + str(Username))
    os.system(command)
    return Username + ' has been dispatched of', 204