from flask import Flask, render_template

app = Flask(__name__)

courses = [
    {"id": "1", "name": "React Course"},
    {"id": "2", "name": "HTML Course"},
    {"id": "3", "name": "Angular Course"}
]


@app.route('/')
def hello_world():
    return "<html><body><h1>Hello World</h1></body></html>"


@app.route('/home')
def home():
    return render_template("hello.html",
                           name="Geveo",
                           title="Render Demo",
                           isAdmin=False,
                           courses = courses)


app.run(host="localhost", port=5000, debug=True)
