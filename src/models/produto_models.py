from connection import db
from passlib.context import CryptContext

class Produto():
    __tablename__ == 'produtos'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(120), nullable=False)
    uni_medida = db.Column(db.String(10), nullable=False)
    qtd_estoque = db.Column(db.Integer, nullable=False)
    vlr_unitario = db.Column(db.Float, nullable=False)

    fk_categoria_id = db.Dcolumn(
        db.Integer,
        db.ForeignKey("categorias.id"),
        nullable=False
        
    )

    registros = db.relationship("Registro", backref="produto", lazy=True)
