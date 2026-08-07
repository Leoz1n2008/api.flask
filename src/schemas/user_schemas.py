from src import ma 
from src.models import user_model
from marshmallow import fields

class UsuarioSchema(ma.SQLALchemyAutoSchema):
    class Meta:
        models = user_model.UsuarioModel
        fields = ('id','nome','email','senha')

    nome = fields.String(required=True)
    email = fields.Email(required=True)
    senha = fields.String(required=True)