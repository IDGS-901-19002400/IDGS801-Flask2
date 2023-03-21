#Importación del framework
from flask import Flask, render_template, request, redirect, make_response, flash
from traductor import TranslateForm
from flask_wtf.csrf import CSRFProtect
from forms import UserForm, LoginForm 
from cajasForm import DinamicBoxForm
from traductor_met import addTranslation, getTranslation
from form import *
from resistencia import *

csrf = CSRFProtect()
app = Flask(__name__)
app.config['SECRET_KEY'] = "peuproweiu"
csrf.init_app(app)

""" @app.get('/')
def index():
    return render_template('form-test.html') """

@app.get('/pupils')
def pupils():
    form = UserForm()
    return render_template('Alumnos.html', form=form)

@app.post('/pupils')
def create_pupil():
    form = UserForm(request.form)
    if not form.validate():
        return render_template('Alumnos.html', form=form)

    print(form.id.data)
    print(form.name.data)
    return render_template('Alumnos.html', form=form)

@app.get('/boxes')
def boxes():
    form = DinamicBoxForm()
    return render_template('cajasDinamicas.html', form=form)

@app.post('/boxes')
def create_boxes():
    form = DinamicBoxForm(request.form)
    inputs_quantity = form.quantity.data
    return render_template('cajasDinamicas.html', form=form, inputs_quantity=inputs_quantity)

@app.post('/caculate-boxes')
def caculate_boxes():
    form = DinamicBoxForm(request.form)
    numbers = [int(number) for number in request.form.getlist('numbers[]')]
    minNum = min(numbers)
    maxNum = max(numbers)
    average = sum(numbers) / len(numbers)
    
    onlyNumbers = set(numbers)
    mapValuesBefore = {}
    mapValues = {}

    for number in onlyNumbers:
        mapValuesBefore[number] = len([num for num in numbers if num == number])

    mapValues = { key: value for key, value in mapValuesBefore.items() if value > 1 }

    return render_template('result-boxes.html', numbers=numbers, minNum=minNum, maxNum=maxNum, average=average, mapValues=mapValues)


@app.get('/translate')
def translate():
    form = TranslateForm()
    return render_template('traductor.html', form=form)

@app.post('/translate')
def create_translate():
    form = TranslateForm(request.form)

    if not form.validate():
        return render_template('traductor.html', form=form)

    addTranslation(form.spanish.data, form.english.data)

    flash("Palabras guardadas!")

    return redirect('/translate')


@app.post('/convert')
def convert():
    form = TranslateForm(request.form)
    
    print(request.form.get('language'))
    translation = getTranslation(form.text.data, request.form.get('language'))

    if translation == False:
     flash("La palabra no fue encontrada","Error")
    else:
     flash("Palabra encontrada")

    return render_template('traductor.html', form=form, translation=translation)
    

@app.get('/cookies')
def cookies():
    form = LoginForm()
    response = make_response(render_template('cookies.html', form=form))

    return response

@app.post('/cookies')
def create_cookies():
    form = LoginForm(request.form)
    response = make_response(render_template('cookies.html', form=form))

    username = form.username.data
    password = form.password.data

    response.set_cookie('data_user', f"{username}@{password}")
    flash(f"Bienvenido {username}")

    return response

@app. context_processor
def utility_processor():
    def getItemColor(item, position):
        if position > 3:
            return [t[1] for t in TOLERANCE if t[0] == item][0] or ''
        return [color[0] for color in COLORS if color[position] == item][0] or 'white'
    return dict(getItemColor=getItemColor)

@app. get('/resistance')
def resistance():
    form = ResistanceForm()
    data = [calculate(*resistance) for resistance in getResistance()] 
    print(data)

    return render_template('resistencia.html', form=form, data = data, colors = COLORS)

@app. post('/resistance')
def create_resistance():
    form  =  ResistanceForm(request. form)
    saveResistance(form. firstBand. data, form. secondBand. data, form. thirdBand. data, form. tolerance. data)
    return redirect('/resistance')

if __name__ == '__main__':
    app.run(debug=True, port=3000)


