from todo import todo
from todo.controller.forms.add_todo import AddTodo
from todo.model.Todos import Todos
from todo.database import db
from flask import render_template, redirect, request


@todo.route('/')
@todo.route('/active')
@todo.route('/complete')
def index():
    form = AddTodo(request.form)

    url_rule = request.url_rule.rule

    if url_rule == '/':
        todos = Todos.query.all()
    elif url_rule == '/active':
        todos = Todos.query.filter_by(todo_complete=False).all()
    elif url_rule == '/complete':
        todos = Todos.query.filter_by(todo_complete=True).all()

    cnt_active_todo = len(Todos.query.filter_by(todo_complete=False).all())
    cnt_complete_todo = len(Todos.query.filter_by(todo_complete=True).all())

    return render_template('index.html', todos=todos, form=form, cnt_active_todo=cnt_active_todo, cnt_complete_todo=cnt_complete_todo)

