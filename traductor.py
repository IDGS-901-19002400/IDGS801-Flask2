from wtforms import StringField, validators
from wtforms import Form

class TranslateForm(Form):
    spanish = StringField('spanish', [validators.DataRequired('El campo es requerido')])
    english = StringField('english', [validators.DataRequired('El campo es requerido')])
    text = StringField('text')
