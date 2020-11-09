from flask_sqlalchemy import *

db = SQLAlchemy()

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
