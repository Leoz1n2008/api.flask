from src.models import CategoriaModel
from src import ma
from marshmallow import fields

class CategoriaSchema(ma.SQLALchemyAutoSchema):
    class meta:
        model = CategoriaModel
        load_instance = True