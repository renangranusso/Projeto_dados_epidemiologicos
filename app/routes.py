from app import app

from flask import render_template

@app.route('/') #raiz do sistema.

def home():
    return render_template('index.html')