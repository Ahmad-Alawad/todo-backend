from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Todo(db.Model):
    __tablename__ = "todo"
    todo_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(64))


def connect_to_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///todos'
    db.app = app
    db.init_app(app)
    db.create_all()
    db.session.commit()
    print('Connected to DB')