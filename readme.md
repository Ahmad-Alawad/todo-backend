## Setup

- pipenv shell
- pip install flask
- pip freeze > requirements.txt
- touch server.py


## Server

``` python

from flask import Flask

app = Flask(__name__)

app.secret_key = "ABC"


if __name__ == "__main__":
	app.run(port=5000, host='0.0.0.0', debug=True)

```

### Add Routes:

#### HTML
```python
from flask import jsonify

@app.route("/", methods=['GET'])
def home():
    return "<h1>Hello Class</h1>"
```

#### JSON
```python
@app.route("/data.json", methods=['GET'])
def data():
    data = {
        "name": "Ahmad",
        "cats": ["Instance", "Cherry"],
        "age": 35
    }
    return jsonify(data)
```

## Models

### Add model

#### Installation
- pip install flask_sqlalchemy

#### model.py - Connect to a database
```python
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_to_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///todos'
    db.app = app
    db.init_app(app)
    db.create_all()
    db.session.commit()
```

#### Add a table
```python
class Todo(db.Model):
    __tablename__ = "todo"
    todo_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(64))
```


#### Connect to db from Server
```python
from model import connect_to_db
connect_to_db(app)
```

#### Routes

##### Get all items
```python
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
```

##### Add Item
```python
from flask import Flask, jsonify, request, redirect
from model import Todo, db
```

```python
@app.route("/add", methods=['GET'])
def add():
    item_name = request.args.get("item")
    item = Todo(name=item_name)
    db.session.add(item)
    db.session.commit()
    return redirect("/all")
```

