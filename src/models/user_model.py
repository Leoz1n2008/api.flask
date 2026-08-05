from connection import db
from passlib.context import CryptContext
                
class Usuario(db.Model):
    __tablename__=='usuario'

    id = db.Column(Integer,primary_key=True,autoincrement=True)
    nome = db.Column(String(100),nullable=False)
    email = db.Column(String(100),nullable=False unique =True)
    senha = db.Column(String(255),nullable=False)

    pwd_context = CryptContext(schemes=['argon2'],deprecated='auto')

    def gen_senha(self,senha):
        self.senha = self.pwd_context.hash(senha)

    def verificar_senha(self,senha):
        return self.pwd_context.verify(senha,self.senha)
	