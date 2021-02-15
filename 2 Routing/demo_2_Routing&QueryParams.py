from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def route_hello_world():
    return "<h1>Hello, World!</h1>"

# string type (default)
@app.route("/hello/<string:name>")
def route_hello(name):
    return f"<h1>Hello, {name}!</h1>" 

# integer type
@app.route("/blog/<int:postId>")
def route_blog(postId):
    return f"<h1>Welcome to blog : blog post - {postId}</h1>"

# float type
@app.route("/documentation/<float:version>")
def route_documentation(version):
    return f"<h1>Documentaion Version - {version}</h1>"

# path type
@app.route("/resources/<path:resource_path>")
def route_resources(resource_path):
    return f"<h1>Resource Path - {resource_path}</h1>"

# query params
@app.route('/search')
def search():
    keyword = request.args.get("keyword")
    sort = request.args.get("sort")
    return f"keyword = {keyword} sort = {sort}"


# starting the development server
app.run(host = "localhost", port = 5000, debug = True)