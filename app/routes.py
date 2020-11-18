from app import app
from flask import render_template
from flask import request
from app.tables import db
from app.tables import Epidemiologico
from app.tables import Doenca

@app.route('/index') #raiz do sistema.
def index():
    return render_template('index.html')


@app.route('/cadastro_doenca', methods=['GET', 'POST'])
def cadastro_doenca():
    if request.method == 'POST':
        doenca = Doenca(request.form['nome'], request.form['sintomas'])
        db.session.add(doenca)
        db.session.commit()
    return render_template('cadastro_doenca.html')

@app.route('/cadastro_epidemiologico', methods=['GET' , 'POST'])
def cadastro_epidemiologico():
    if request.method == 'POST':
        if request.form['data_coleta'] != "" and request.form['doenca_associada'] != "":
            epidemio = Epidemiologico(request.form['data_coleta'], request.form['doenca_associada'])
            db.session.add(epidemio)
            db.session.commit()
    return render_template('cadastro_epidemiologico.html')

@app.route('/visualizacao_doencas', methods=['GET'])
def visualizacao_doencas():
    doenca = Doenca.query.all()
    return render_template('visualizacao_doencas.html', doenca=doenca)

@app.route('/visualizacao_epidemiologica', methods=['GET'])
def visualizacao_epidemiologica():
    Epidemio = Epidemiologico.query.all()
    return render_template('visualizacao_epidemiologica.html', Epidemio=Epidemio)
