from connection import db
from src.models.categoria_models import Categoria


def criar_categoria(dados):

    categoria = Categoria(
        descricao=dados["descricao"]
    )

    db.session.add(categoria)
    db.session.commit()

    return categoria


def listar_categorias():

    return Categoria.query.all()


def buscar_categoria(id):

    return Categoria.query.get(id)


def atualizar_categoria(id, dados):

    categoria = Categoria.query.get(id)

    if not categoria:
        return None

    if "descricao" in dados:
        categoria.descricao = dados["descricao"]

    db.session.commit()

    return categoria


def excluir_categoria(id):

    categoria = Categoria.query.get(id)

    if not categoria:
        return False

    db.session.delete(categoria)
    db.session.commit()

    return True