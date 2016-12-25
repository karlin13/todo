from todo import todo
from todo.model.Todos import Todos
from todo.database import db
from flask import request, redirect


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

