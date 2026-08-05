from connection import db
from passlib.context import CryptContext

class Categoria():
    __tablename__ = 'categorias'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    descricao = db.Column(db.String(120), nullable=False)

    produtos = db.relationship("Produto", backref="categoria", lazy=True)
