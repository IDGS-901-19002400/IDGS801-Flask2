from wtforms import StringField, validators
from wtforms import Form

class TranslateForm(Form):
    spanish = StringField('Español', [validators.DataRequired('El campo es requerido')])
    english = StringField('Ingles', [validators.DataRequired('El campo es requerido')])
    text = StringField('Agrega el texto')
