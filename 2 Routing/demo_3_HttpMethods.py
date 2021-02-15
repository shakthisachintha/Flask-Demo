from flask import Flask, request

app = Flask(__name__)

local_dataset = {"courses": [
    {"id": "1", "name": "React Course"},
    {"id": "2", "name": "HTML Course"},
    {"id": "3", "name": "Angular Course"}]
}


@app.route("/courses", methods=['GET', 'POST'])
def course_resource_get_post():
    if request.method == 'GET':
        return local_dataset

    if request.method == 'POST':
        local_dataset["courses"].append(
            {"id": request.form['id'],
             "name": request.form['name']
             })
        return local_dataset


@app.route("/courses/<id>", methods = ['PUT', 'DELETE'])
def course_resource_put_delete(id):
    if request.method == 'PUT':
        for c in local_dataset["courses"]:
            if c["id"] == id :
                c["name"] = request.form['name']
        return local_dataset


    # starting the development server
app.run(host="localhost", port=5000, debug=True)
