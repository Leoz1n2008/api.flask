from connection import db
from src.models.user_models import Usuario


def criar_usuario(dados):

    usuario = Usuario(
        nome=dados["nome"],
        email=dados["email"]
    )

    usuario.gen_senha(dados["senha"])

    db.session.add(usuario)
    db.session.commit()

    return usuario


def listar_usuarios():
    return Usuario.query.all()


def buscar_usuario(id):
    return Usuario.query.get(id)


def buscar_usuario_email(email):
    return Usuario.query.filter_by(email=email).first()


def atualizar_usuario(id, dados):

    usuario = Usuario.query.get(id)

    if not usuario:
        return None

    if "nome" in dados:
        usuario.nome = dados["nome"]

    if "email" in dados:
        usuario.email = dados["email"]

    if "senha" in dados:
        usuario.gen_senha(dados["senha"])

    db.session.commit()

    return usuario


def excluir_usuario(id):

    usuario = Usuario.query.get(id)

    if not usuario:
        return False

    db.session.delete(usuario)
    db.session.commit()

    return True


def verificar_login(email, senha):

    usuario = Usuario.query.filter_by(
        email=email
    ).first()

    if not usuario:
        return None

    if usuario.verifica_senha(senha):
        return usuario

    return None