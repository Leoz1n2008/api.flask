from flask_restful import Resource
from flask import request, jsonify, make_response
from marshmallow import ValidationError

from src import api
from src.schemas.category_schema import categoria_schema, categorias_schema
from src.services import categoria_services


class CategoriaList(Resource):
    def get(self):
        """
        Lista todas as categorias.
        ---
        tags:
            - Categorias
        responses:
            200:
                description: Lista de categorias
            404:
                description: Nenhuma categoria cadastrada
        """
        categorias = categoria_services.listar_categorias()

        if not categorias:
            return make_response(jsonify({'message': 'Não existem categorias!'}), 404)

        return make_response(jsonify(categorias_schema.dump(categorias)), 200)

    def post(self):
        """
        Cria uma nova categoria.
        ---
        tags:
            - Categorias
        parameters:
            - in: body
              name: body
              required: true
              schema:
                type: object
                properties:
                    descricao:
                        type: string
        responses:
            201:
                description: Categoria criada com sucesso
            400:
                description: Erro de validação
        """
        try:
            categoria = categoria_schema.load(request.get_json())
        except ValidationError as err:
            return err.messages, 400

        try:
            resultado = categoria_services.criar_categoria(categoria)
            return categoria_schema.dump(resultado), 201
        except Exception as e:
            return {"message": str(e)}, 400


class CategoriaResource(Resource):
    def get(self, id_categoria):
        """
        Busca uma categoria por ID.
        ---
        tags:
            - Categorias
        parameters:
            - name: id_categoria
              in: path
              type: integer
              required: true
        responses:
            200:
                description: Categoria encontrada
            404:
                description: Categoria não encontrada
        """
        categoria = categoria_services.buscar_categoria(id_categoria)
        if not categoria:
            return {"message": "Categoria não encontrada!"}, 404

        return categoria_schema.dump(categoria), 200

    def put(self, id_categoria):
        """
        Atualiza uma categoria.
        ---
        tags:
            - Categorias
        parameters:
            - name: id_categoria
              in: path
              type: integer
              required: true
            - in: body
              name: body
              required: true
              schema:
                type: object
                properties:
                    descricao:
                        type: string
        responses:
            200:
                description: Categoria atualizada
            404:
                description: Categoria não encontrada
        """
        try:
            nova_categoria = categoria_schema.load(request.get_json())
        except ValidationError as err:
            return err.messages, 400

        categoria = categoria_services.editar_categoria(id_categoria, {
            "descricao": nova_categoria.descricao
        })

        if not categoria:
            return {"message": "Categoria não encontrada!"}, 404

        return categoria_schema.dump(categoria), 200

    def delete(self, id_categoria):
        """
        Deleta uma categoria.
        ---
        tags:
            - Categorias
        parameters:
            - name: id_categoria
              in: path
              type: integer
              required: true
        responses:
            200:
                description: Categoria deletada com sucesso
            404:
                description: Categoria não encontrada
        """
        if categoria_services.deletar_categoria(id_categoria):
            return {"message": "Categoria deletada com sucesso!"}, 200
        return {"message": "Categoria não encontrada!"}, 404


api.add_resource(CategoriaList, '/categorias')
api.add_resource(CategoriaResource, '/categoria/<int:id_categoria>')