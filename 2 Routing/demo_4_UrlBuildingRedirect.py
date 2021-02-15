from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/redirect/<user_type>/<user_name>')
def index(user_type, user_name):
    if user_type == "admin":
        return redirect(url_for("hello_admin", name = user_name))
    if user_type == "customer":
        return redirect(url_for("hello_customer", name = user_name))

@app.route("/admin/<name>")
def hello_admin(name):
    return f"<h1>Hello, Admin ({name})</h1>"

@app.route("/customer/<name>")
def hello_customer(name):
    return f"<h1>Hello, Customer ({name})</h1>"

app.run(host = "localhost", port = 5000, debug = True)