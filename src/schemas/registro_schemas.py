from SRC import ma
from SRC.MODELS import RegistroModel
from marshmallow import fields, validate

class RegistroSchemas(ma.SQLAlchmeyAutoSchema):
    class Meta:
        model = RegistroModel
        fields = ('id','dth_registro', 'Qtd_produto', 'id_produto' )
    dth_registro = fields.DateTime(required= True)
    tipo = fields.Bool(required= True)
    Qtd_produto = fields.Integer(required= True, 
                                 validate= validate.Range(min = 0, error= 'Valor deve ser maior que 0'))
    id_produto = fields.Integer(required= True)