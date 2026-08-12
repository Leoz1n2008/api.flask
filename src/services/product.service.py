from connection import db
from src.models.produto_models import Produto


def criar_produto(dados):
    produto = Produto(
        nome=dados["nome"],
        uni_medida=dados["uni_medida"],
        qtd_estoque=dados["qtd_estoque"],
        vlr_unitario=dados["vlr_unitario"],
        fk_categoria_id=dados["fk_categoria_id"]
    )

    db.session.add(produto)
    db.session.commit()

    return produto


def listar_produtos():
    return Produto.query.all()


def buscar_produto(id):
    return Produto.query.get(id)


def atualizar_produto(id, dados):
    produto = Produto.query.get(id)

    if not produto:
        return None

    if "nome" in dados:
        produto.nome = dados["nome"]

    if "uni_medida" in dados:
        produto.uni_medida = dados["uni_medida"]

    if "qtd_estoque" in dados:
        produto.qtd_estoque = dados["qtd_estoque"]

    if "vlr_unitario" in dados:
        produto.vlr_unitario = dados["vlr_unitario"]

    if "fk_categoria_id" in dados:
        produto.fk_categoria_id = dados["fk_categoria_id"]

    db.session.commit()

    return produto


def excluir_produto(id):
    produto = Produto.query.get(id)

    if not produto:
        return False

    db.session.delete(produto)
    db.session.commit()

    return True