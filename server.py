from flask import Flask, jsonify, request, redirect
from model import Todo, db

app = Flask(__name__)

app.secret_key = "ABC"


@app.route("/", methods=['GET'])
def home():
    return "<h1>Hello Class</h1>"

@app.route("/data.json", methods=['GET'])
def data():
    data = {
        "name": "Ahmad",
        "cats": ["Instance", "Cherry"],
        "age": 35
    }
    return jsonify(data)


@app.route("/add", methods=['GET'])
def add():
    item_name = request.args.get("item")
    item = Todo(name=item_name)
    db.session.add(item)
    db.session.commit()
    return redirect("/all")

@app.route("/all", methods=['GET'])
def all_items():
    todos = Todo.query.all()
    all_todos = []
    for t in todos:
        all_todos.append(t.name)
    # print(type(all_todos[0]))
    # data = {'all': all_items}
    # return jsonify([t.name for t in todos])
    return jsonify(all_todos)


if __name__ == "__main__":
	from model import connect_to_db
	connect_to_db(app)
	app.run(port=5000, host='0.0.0.0', debug=True)