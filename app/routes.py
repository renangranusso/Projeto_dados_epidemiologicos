from app import app
from flask import render_template, request, redirect, url_for
from app.tables import db
from app.tables import Epidemiologico
from app.tables import Doenca

@app.route('/index') #raiz do sistema.
def index():
    return render_template('index.html')


@app.route('/cadastro_doenca', methods=['GET'])
def cadastro_doenca():
    return render_template('cadastro_doenca.html')

@app.route('/processo_doenca', methods=['POST'])
def processo_doenca():
    if request.method == 'POST':
        doenca = Doenca(request.form['doenca'], request.form['sintomas'])
        db.session.add(doenca)
        db.session.commit()
        return redirect(url_for('cadastro_doenca'))


@app.route('/cadastro_epidemiologico', methods=['GET'])
def cadastro_epidemiologico():
    return render_template('cadastro_epidemiologico.html')

@app.route('/processo_epidemio', methods=['POST'])
def processo_epidemio():
    if request.method == 'POST':
        epidemio = Epidemiologico(request.form['data_coleta'], request.form['doenca_associada'])
        db.session.add(epidemio)
        db.session.commit()
        return redirect(url_for('cadastro_epidemiologico'))


@app.route('/visualizacao_doencas', methods=['GET'])
def visualizacao_doencas():
    doenca = Doenca.query.all()
    return render_template('visualizacao_doencas.html', doenca=doenca)

@app.route('/delete/<int:id>')
def remover(id):
    doenca = Doenca.query.get(id)
    db.session.delete(doenca)
    db.session.commit()
    return redirect(url_for('visualizacao_doencas'))

@app.route('/visualizacao_epidemiologica', methods=['GET'])
def visualizacao_epidemiologica():
    Epidemio = Epidemiologico.query.all()
    return render_template('visualizacao_epidemiologica.html', Epidemio=Epidemio)
