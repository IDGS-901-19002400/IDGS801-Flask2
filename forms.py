
from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FieldList, FormField, SelectField

from wtforms.fields import EmailField, TextAreaField, RadioField, PasswordField

class UserForm(Form):
   
   matricula = StringField('Matricula')
   nombre = StringField ('Nombre')
   apaterno = StringField('Apellido Paterno')
   amaterno = StringField('Apellido Materno')
   email = StringField('Correo Electronico')


