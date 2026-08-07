from SRC.MODELS import ProdutoModel
from SRC import ma
from marshmallow import fields, validate
from categoria_schemas import CategoriaSchema
class ProdutoSchema(ma.SQLAlchemyAutoSchema):
    categoria = fields.Nested(
        CategoriaSchema,
        dump_only= True
    )

    class Meta:
        model = ProdutoModel
        load_instance = True
        include_fk = True
    nome = fields.String(required= True)
    Uni_medida = fields.String(required= True)
    Qtd_estoque = fields.Integer(required= True, 
                                 validate= validate.Range(min=0, error='A quantidade deve ser maior ou igual a 0 '))
    Vlr_unitario = fields.Decimal(required= True,
                                  places= 2,
                                  validate= validate.Range(min=0, error= 'O valor unitario deve ser maior ou igual a 0 '))
    id_categoria = fields.Integer(required= True) 

produto_schema = ProdutoSchema()