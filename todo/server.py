from flask import Flask, render_template, request, redirect
from database import init_db, db_session
from todosModel import todos
from todoInputForm import todoInputForm

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    form = todoInputForm(request.form)
    if request.method == 'POST' and form.validate():
        todo = todos(todo=form.todo.data, is_complete=False)
        db_session.add(todo)
        db_session.commit()
    todos_list = todos.query.all()

    todo_active_list = todos.query.filter_by(is_complete=False).all()

    return render_template("index.html", form = form, todos = todos_list, todos_len = len(todo_active_list))

@app.route('/active', methods=['GET', 'POST'])
def active():
    form = todoInputForm(request.form)
    if request.method == 'POST' and form.validate():
        todo = todos(todo=form.todo.data, is_complete=False)
        db_session.add(todo)
        db_session.commit()
    todos_list = todos.query.filter_by(is_complete=False).all()

    return render_template("index.html", form=form, todos=todos_list, todos_len=len(todos_list) )

@app.route('/complete', methods=['GET', 'POST'])
def complete():
    form = todoInputForm(request.form)
    if request.method == 'POST' and form.validate():
        todo = todos(todo=form.todo.data, is_complete=False)
        db_session.add(todo)
        db_session.commit()
    todos_list = todos.query.filter_by(is_complete=True).all()

    todo_active_list = todos.query.filter_by(is_complete=False).all()

    return render_template("index.html", form=form, todos=todos_list, todos_len=len(todo_active_list))

@app.route('/tododone')
def todo_done():
    todo_id = request.values['todostate']
    todo = todos.query.filter_by(id=todo_id).first()

    todo.is_complete = True
    db_session.commit()

    return redirect(request.referrer, code=302)

@app.route('/todoundone')
def todo_undone():
    todo_id = request.values['todostate']
    todo = todos.query.filter_by(id=todo_id).first()

    todo.is_complete = False
    db_session.commit()

    return redirect(request.referrer, code=302)

@app.route('/clearall')
def clear_all():
    todo_list = todos.query.all()

    for todo in todo_list:
        db_session.delete(todo)

    db_session.commit()

    return redirect(request.referrer, code="302")

@app.route('/delete')
def delete():
    todo_id = request.values['remove']
    todo = todos.query.filter_by(id=todo_id).first()
    db_session.delete(todo)
    db_session.commit()

    return redirect(request.referrer, code=302)

if __name__ == '__main__':
    init_db()
    app.run()
