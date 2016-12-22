from database import db


class Todos(db.Model):
    __tablename__ = 'todos'
    id = db.Column(db.Integer, primary_key=True)
    todo = db.Column(db.String(100), unique=False) #TODO: test if 'unique=False' is default
    todo_complete = db.Column(db.Boolean)

    def __init__(self, todo, todo_complete):
        self.todo = todo
        self.todo_complete = todo_complete
