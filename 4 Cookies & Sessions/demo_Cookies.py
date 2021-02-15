from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/set-cookie/<name>')
def set_cookie(name):
    resp = make_response("<h3>Cookie Set</h3>")
    resp.set_cookie('name', name)
    return resp

@app.route('/get-cookie')
def get_cookie():
    name = request.cookies.get('name')
    return f"<h3>Cookie Value is { name }</h3>"


app.run(host = "localhost", port = 5000, debug = True)