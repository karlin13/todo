from flask import Flask, render_template, request, redirect, url_for
from todosModel import Todos
from database import db, init_db
from inputForm import InputForm


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test1.db"


@app.route('/', methods=['GET', 'POST'])
@app.route('/active', methods=['GET', 'POST'])
@app.route('/complete', methods=['GET', 'POST'])
def index():
    form = InputForm(request.form)

    if request.method == 'POST' and form.validate():
        todo = Todos(todo=form.input.data, todo_complete=False)
        db.session.add(todo)
        db.session.commit()

    url_rule = request.url_rule.rule

    if url_rule == '/':
        todos = Todos.query.all()
    elif url_rule == '/active':
        todos = Todos.query.filter_by(todo_complete=False).all()
    elif url_rule == '/complete':
        todos = Todos.query.filter_by(todo_complete=True).all()

    cnt_active_todo = len(Todos.query.filter_by(todo_complete=False).all())
    cnt_complete_todo=len(Todos.query.filter_by(todo_complete=True).all())

    return render_template('index.html', todos=todos, form=form, cnt_active_todo=cnt_active_todo, cnt_complete_todo=cnt_complete_todo)


@app.route('/done', methods=['POST'])
def done():
    todo_id = request.values.get('todo_id')
    todo = Todos.query.filter_by(id=todo_id).first()

    todo.todo_complete = True

    db.session.commit()

    return redirect(url_for('index'), code=304)


@app.route('/not_done', methods=['POST'])
def not_done():

    todo_id = request.values.get('todo_id')
    todo = Todos.query.filter_by(id=todo_id).first()

    todo.todo_complete = False

    db.session.commit()

    return redirect(request.referrer, code=304)


@app.route('/remove', methods=['POST'])
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


@app.route('/remove_completed', methods=['POST'])
def remove_completed():
    '''
    remove all completed todos
    :return:
    '''
    completed_todos = Todos.query.filter_by(todo_complete=True).all()

    for completed_todo in completed_todos:
        db.session.delete(completed_todo)

    db.session.commit()

    return redirect(request.referrer, code=304)


if __name__ == "__main__":
    init_db(app)
    app.run(debug=True, port=8080)