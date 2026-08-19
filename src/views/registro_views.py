from flask import Blueprint, request, jsonify
from marshmallow import ValidationError

from src.schemas.register_schemas import RegistroSchema
from src.services.register_services import (
    criar_registro,
    listar_registros,
    buscar_registro,
    atualizar_registro,
    excluir_registro
)


register_bp = Blueprint(
    "registros",
    __name__,
    url_prefix="/registros"
)

registro_schema = RegistroSchema()
registros_schema = RegistroSchema(many=True)


@register_bp.route("/", methods=["GET"])
def get_registros():

    registros = listar_registros()

    return jsonify(
        registros_schema.dump(registros)
    ), 200


@register_bp.route("/<int:id>", methods=["GET"])
def get_registro(id):

    registro = buscar_registro(id)

    if not registro:
        return jsonify({
            "erro": "Registro não encontrado"
        }), 404

    return jsonify(
        registro_schema.dump(registro)
    ), 200


@register_bp.route("/", methods=["POST"])
def post_registro():

    dados = request.get_json()

    if not dados:
        return jsonify({
            "erro": "Nenhum dado foi enviado"
        }), 400

    try:
        registro_schema.load(dados)

    except ValidationError as erro:
        return jsonify({
            "erros": erro.messages
        }), 400

    registro = criar_registro(dados)

    return jsonify(
        registro_schema.dump(registro)
    ), 201


@register_bp.route("/<int:id>", methods=["PUT"])
def put_registro(id):

    registro = buscar_registro(id)

    if not registro:
        return jsonify({
            "erro": "Registro não encontrado"
        }), 404

    dados = request.get_json()

    if not dados:
        return jsonify({
            "erro": "Nenhum dado foi enviado"
        }), 400

    try:
        registro_schema.load(
            dados,
            partial=True
        )

    except ValidationError as erro:
        return jsonify({
            "erros": erro.messages
        }), 400

    registro = atualizar_registro(
        id,
        dados
    )

    return jsonify(
        registro_schema.dump(registro)
    ), 200


@register_bp.route("/<int:id>", methods=["DELETE"])
def delete_registro(id):

    registro = buscar_registro(id)

    if not registro:
        return jsonify({
            "erro": "Registro não encontrado"
        }), 404

    excluir_registro(id)

    return jsonify({
        "mensagem": "Registro excluído com sucesso"
    }), 200