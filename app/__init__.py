#pacote do python / instancia da aplicação

from flask import Flask

app = Flask(__name__) #Instancia da classe FLASK (para ciração do aplicativo)

from app import routes