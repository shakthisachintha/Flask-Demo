from flask import Flask, session, redirect, url_for

app = Flask(__name__)

app.secret_key = "my_secret_key"

@app.route("/")
def index():
    if 'username' in session:
        return f"Logged in as {session['username']}"
    else:
        return "You are not logged in"

@app.route("/login/<username>")
def login(username):
    session["username"] = username
    return redirect(url_for("index"))

@app.route("/logout")
def logout():
    session.pop('username')
    return redirect(url_for("index"))

app.run(host = "localhost", port = 5000, debug = True)