from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

app.run(host = "localhost", port = 5000, debug = True)