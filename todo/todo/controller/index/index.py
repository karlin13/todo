from todo import todo
from todo.controller.forms.add_todo import AddTodo
from todo.model.Todos import Todos
from todo.database import db
from flask import render_template, redirect, request


@todo.route('/', methods=['GET', 'POST'])
@todo.route('/active', methods=['GET', 'POST'])
@todo.route('/complete', methods=['GET', 'POST'])
def index():
    form = AddTodo(request.form)

    if request.method == 'POST' and form.validate():
        new_todo = Todos(todo=form.input.data, todo_complete=False)
        db.session.add(new_todo)
        db.session.commit()

        return redirect(request.referrer)

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


@todo.route('/done', methods=['POST'])
def done():
    todo_id = request.values.get('todo_id')
    active_todo = Todos.query.filter_by(id=todo_id).first()

    active_todo.todo_complete = True

    db.session.commit()

    return redirect(request.referrer, code=304)


@todo.route('/not_done', methods=['POST'])
def not_done():

    todo_id = request.values.get('todo_id')
    complete_todo = Todos.query.filter_by(id=todo_id).first()

    complete_todo.todo_complete = False

    db.session.commit()

    return redirect(request.referrer, code=304)


#   명료한 이름을 생각 못하겠음
@todo.route('/all', methods=['POST'])
def all():

    state = (request.form.get('state') == 'true')
    opposite_state = not state

    opposite = Todos.query.filter_by(todo_complete=opposite_state).all()

    for todo in opposite:
        todo.todo_complete = state

    db.session.commit()

    return redirect(request.referrer, code=304)


@todo.route('/remove', methods=['POST'])
def remove():
    '''
    remove only selected todo
    :return:
    '''
    todo_id = request.form.get('todo_id')
    todo = Todos.query.filter_by(id=todo_id).first()

    print(todo_id)

    db.session.delete(todo)
    db.session.commit()

    return redirect(request.referrer, code=304)


@todo.route('/remove_completed', methods=['POST'])
def remove_completed():
    '''
    remove all completed todos
    :return:
    '''
    completed_todos = Todos.query.filter_by(todo_complete=True).all()

    for completed_todo in completed_todos:
        db.session.delete(completed_todo)

    db.session.commit()
    db.session.commit()

    return redirect(request.referrer, code=304)

