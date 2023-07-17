from datetime import datetime as dt
from http import HTTPStatus
import time
import secrets
from flask import Flask, session, redirect, url_for, request


app = Flask(__name__)
app.secret_key = secrets.token_hex(64)

def createResponseBody(start, args = None):
    ret = {
        "timestamp": dt.now().strftime('%F %T.%f')[:-3],  
    }

    if args is not None:
        for i in args:
            ret[i] = args[i]

    ret["duration"] = round(time.time() - start, 3)    

    return ret

@app.route("/ping", methods=['GET'])
def ping():
    start = time.time()

    app.logger.info("Ping request received")

    return createResponseBody(start)

@app.route('/')
def index():
    if 'username' in session:
        return f'Logged in as {session["username"]}'
    return 'You are not logged in'
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))