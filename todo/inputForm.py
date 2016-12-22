from wtforms import StringField, Form, validators

class InputForm(Form):
    input = StringField([validators.Length(min=1, max=100)])
