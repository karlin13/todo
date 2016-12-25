from wtforms import StringField, Form, validators

class AddTodo(Form):
    input = StringField([validators.Length(min=1, max=100)])
