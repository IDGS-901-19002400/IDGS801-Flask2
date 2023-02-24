from wtforms import FieldList, Form
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, Field, FormField, SelectField, RadioField, IntegerField
from wtforms.fields import EmailField

class DinamicBoxForm(Form):
    quantity = IntegerField('quantity')
    numbers = FieldList(StringField('numbers'))



