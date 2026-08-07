from flask import Flask
from connection import db, Config
from flask_marshmallow import Marshmallow

ma = Marshmallow()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    ma.init_app(app)

    #Verifica o funcionamento do server (opcional)
    @app.get('/')
    def home():
        return{"mensagem" : "API Flask Funcionando"}, 200

    return app    