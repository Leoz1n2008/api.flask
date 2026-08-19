from flask import Flask
from connection import db, config
from flask_marshmallow import Marshmallow
from flask_restful import Api 
from flasgger import Swagger
ma = Marshmallow()
api = Api()

from .models.user_model import UsuarioModels
from .views import user_views

def creat_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    ma.init_app(app)
    api.init_app(app)
    swagger = Swagger(app,config={
        #configuração de cabeçalho
        "headers":[],
        "specs":[
            {
                #http://localhost:5000/apispec.json
                "endpoint":"asispec",
                "route":"asispec.json",
                #incluir rotas
                "rule_filter": lambda rule:True,
                #incluir models
                "model_filter":lambda tag:True
            }
        ],
        "static_url_path":"/flasgger_static",
        "swagger_ui":True,
        "specs_route": "/docs"
    })

    #Verifica o funcionamento do server (opcional)
    @app.get('/')
    def home():
        return{"mensagem" : "API Flask Funcionando"}, 200

    return app    