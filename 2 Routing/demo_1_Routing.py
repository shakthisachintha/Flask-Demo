from flask import Flask

app = Flask(__name__)

# hello world route
# def route_hello_world():
#     return "Hello, World!"
# app.add_url_rule(rule = "/", view_func = route_hello_world)


@app.route("/")
def route_hello_world():
    return "<h1>Hello, World!</h1>" 


# contact route
def route_contact():
    return "Contact us"
app.add_url_rule(rule = "/contact", view_func = route_contact)


# blog route
def route_blog():
    return "<h1>Welcome to blog</h1>"
app.add_url_rule(rule = "/blog", view_func = route_blog)

# starting the development server
app.run(host = "localhost", port = 5000, debug = True)