
from wtforms import Form, validators
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, Field, FormField, SelectField, RadioField
from wtforms.fields import EmailField

def mi_validacion(form, field):
    if len(field.data) == 0:
        raise validators.ValidationError('El campo no tiene datos')

class UserForm(Form):
    id = StringField('id', [
        validators.DataRequired('El campo es requerido'),
        validators.length(min=5, max=10, message='Ingresa min 5 max 10'),
        ])
    name = StringField('name', [validators.DataRequired(message='El campo es requerido')])
    lastname = StringField('lastname', [mi_validacion])
    email = EmailField('email')

class LoginForm(Form):
    username = StringField('username', [
            validators.DataRequired(message='El campo es requerido'),
            validators.length(min=5, max=10, message='Ingresa min 5 max 10'),
        ])
    password = StringField('password', [
            validators.DataRequired(message='El campo es requerido'),
            validators.length(min=5, max=10, message='Ingresa min 5 max 10'),
        ])

 


