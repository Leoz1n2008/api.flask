from flask import Flask
from connection import db, config

def creat_app():
    app = Flask(__name__)
    db.init_app(app)

    #Verifica o funcionamento do server (opcional)
    @app.get('/')
    def home():
        return{"mensagem" : "API Flask Funcionando"}, 200

    return app    