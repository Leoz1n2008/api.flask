from connection import db
from passlib.context import CryptContext

class Registro():
    __tablename__ == 'registros'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    dth_registro = db.Column(db.DateTime, default=datetime.utcnow)
    tipo = db.Column(db.Boolean, nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)

    fk_produto_id = db.Column(
        db.Integer,
        db.ForeignKey("produtos.id"),
        nullable=False
    )