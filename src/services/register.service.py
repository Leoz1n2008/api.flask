from connection import db
from src.models.registro_models import Registro


def criar_registro(dados):
    registro = Registro(
        tipo=dados["tipo"],
        quantidade=dados["quantidade"],
        fk_produto_id=dados["fk_produto_id"]
    )

    db.session.add(registro)
    db.session.commit()

    return registro


def listar_registros():
    return Registro.query.all()


def buscar_registro(id):
    return Registro.query.get(id)


def atualizar_registro(id, dados):
    registro = Registro.query.get(id)

    if not registro:
        return None

    if "tipo" in dados:
        registro.tipo = dados["tipo"]

    if "quantidade" in dados:
        registro.quantidade = dados["quantidade"]

    if "fk_produto_id" in dados:
        registro.fk_produto_id = dados["fk_produto_id"]

    db.session.commit()

    return registro


def excluir_registro(id):
    registro = Registro.query.get(id)

    if not registro:
        return False

    db.session.delete(registro)
    db.session.commit()

    return True