from app import app

if __name__ == "__main__": #verificar o contexto que está sendo executado o modulo de controle.
    app.run(debug=True, port=80)
