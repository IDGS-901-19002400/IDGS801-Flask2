from wtforms import Form
from wtforms import StringField, IntegerField
from wtforms.fields import FieldList

class MyForm(Form):
    cantidad = IntegerField('cantidad')
    numeros = FieldList(StringField('numero'), min_entries=1, max_entries=100)
