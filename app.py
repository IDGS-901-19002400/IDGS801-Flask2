#Importación del framework
from flask import Flask,render_template, request
from flask_wtf.csrf import CSRFProtect
from cajasForm import MyForm

import forms

#Nombre del app
app = Flask(__name__)

@app.route('/calcular', methods=['GET'])
def calcular():
    return render_template("calcular.html") #render_template muestra el html



@app.route('/Alumnos',methods=['GET', 'POST'])
def alumnos():
    reg_alumno = forms.UserForm(request.form)
    mat = ''
    nom = ''

    if request.method == 'POST':
        pass

        mat = reg_alumno.matricula.data
        nom = reg_alumno.nombre.data

    return render_template('Alumnos.html',form=reg_alumno)



csrf = CSRFProtect()
app = Flask(__name__)
app.config['SECRET_KEY'] = "luna"
csrf.init_app(app)

@app.route('/cajas', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        formulario = MyForm()
        return render_template('cajasDinamicas.html', form=formulario)
    else:
        formulario = MyForm(request.form)
        return render_template('cajasDinamicas.html', form=formulario)
     
@app.route('/resultado', methods=['POST'])
def resultado():
    formulario = MyForm(request.form)
    valores = [int(number) for number in formulario.numeros.data]
    
    repetidos = []
 
    for valor in set(valores):
        repeticiones = len([num for num in valores if num == valor])
        if repeticiones > 1:
            repetidos.append((valor, repeticiones))

    return render_template('resultados.html', valores=valores, minNum=min(valores), maxNum=max(valores), promedio=sum(valores) / len(valores), repetidos=repetidos)




if __name__ == "__main__":
    app.run(debug = True, port=3000)

