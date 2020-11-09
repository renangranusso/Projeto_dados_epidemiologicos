#pacote do python / instancia da aplicação

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.tables import db

app = Flask(__name__) #Instancia da classe FLASK (para ciração do aplicativo).

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1234@localhost/bd_trabalho'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

from app import routes
