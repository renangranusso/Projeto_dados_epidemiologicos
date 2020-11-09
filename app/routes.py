from app import app
from flask import render_template
from flask import request
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1234@localhost/bd_trabalho'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Doenca(db.Model):
    __tablename__ = 'Doenca'
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    nome = db.Column(db.String(100))
    sintomas = db.Column(db.String(100))

    def __init__(self, nome, sintomas):
        self.nome = nome
        self.sintomas = sintomas

class Epidemiologico(db.Model):
    __tablename__ = 'Epidemiologico'
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    data_coleta = db.Column(db.String(10))
    doenca_associada = db.Column(db.String(100))

    def __init__(self, data_coleta, doenca_associada):
        self.data_coleta = data_coleta
        self.doenca_associada = doenca_associada

db.create_all()

@app.route('/index') #raiz do sistema.
def index():
    return render_template('index.html')


@app.route('/cadastro_doenca', methods=['GET', 'POST'])
def cadastro_doenca():
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
    return render_template('visualizacao_doencas.html')

@app.route('/visualizacao_epidemiologica', methods=['GET'])
def visualizacao_epidemiologica():
    Epidemio = Epidemiologico.query.all()
    return render_template('visualizacao_epidemiologica.html', Epidemio=Epidemio)