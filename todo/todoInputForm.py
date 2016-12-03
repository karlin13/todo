from wtforms import StringField, Form, validators


class todoInputForm(Form):
    todo = StringField([validators.Length(min=4, max=25)])