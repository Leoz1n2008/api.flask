from flask_restful import Resource
from flask import request, jsonify, make_response
from src.schemas.product_schemas import (produto_schema, produtos_schema)
from marshmallow import ValidationError
from src.services import produto_services
from src import api


class ProdutoList(Resource):
    def get(self):
        """
        Lista todos os produtos.
        ---
        tags:
            - Produtos
        responses:
            200:
                description: Lista de produtos
            404:
                description: Nenhum produto cadastrado
        """
        produtos = produto_services.listar_produtos()

        if not produtos:
            return make_response(jsonify({'message': 'Não existem produtos!'}), 404)

        return make_response(jsonify(produtos_schema.dump(produtos)), 200)

    def post(self):
        """
        Cria um novo produto.
        ---
        tags:
            - Produtos
        parameters:
            - in: body
              name: body
              required: true
              schema:
                type: object
                properties:
                    nome:
                        type: string
                    preco:
                        type: number
                    uni_medida:
                        type: string
                    qtd_estoque:
                        type: integer
                    id_categoria:
                        type: integer
        responses:
            201:
                description: Produto criado com sucesso
            400:
                description: Erro de validação
        """
        try:
            produto = produto_schema.load(request.get_json())
        except ValidationError as err:
            return err.messages, 400

        try:
            resultado = produto_services.criar_produto(produto)
            return produto_schema.dump(resultado), 201
        except Exception as e:
            return {"message": str(e)}, 400


class ProdutoResource(Resource):
    def get(self, id_produto):
        """
        Busca um produto por ID.
        ---
        tags:
            - Produtos
        parameters:
            - name: id_produto
              in: path
              type: integer
              required: true
        responses:
            200:
                description: Produto encontrado
            404:
                description: Produto não encontrado
        """
        produto = produto_services.buscar_produto(id_produto)
        if not produto:
            return {"message": "Produto não encontrado!"}, 404
        return produto_schema.dump(produto), 200

    def put(self, id_produto):
        """
        Atualiza um produto.
        ---
        tags:
            - Produtos
        parameters:
            - name: id_produto
              in: path
              type: integer
              required: true
            - in: body
              name: body
              required: true
              schema:
                type: object
                properties:
                    nome:
                        type: string
                    preco:
                        type: number
                    uni_medida:
                        type: string
                    qtd_estoque:
                        type: integer
                    id_categoria:
                        type: integer
        responses:
            200:
                description: Produto atualizado
            404:
                description: Produto não encontrado
        """
        try:
            novo_produto = produto_schema.load(request.get_json())
        except ValidationError as err:
            return err.messages, 400

        produto = produto_services.atualizar_produto(id_produto, {
            "nome": novo_produto.nome,
            "preco": getattr(novo_produto, 'preco', None),
            "uni_medida": getattr(novo_produto, 'uni_medida', None),
            "qtd_estoque": getattr(novo_produto, 'qtd_estoque', None),
            "id_categoria": getattr(novo_produto, 'id_categoria', None)
        })

        if not produto:
            return {"message": "Produto não encontrado!"}, 404

        return produto_schema.dump(produto), 200

    def delete(self, id_produto):
        """
        Deleta um produto.
        ---
        tags:
            - Produtos
        parameters:
            - name: id_produto
              in: path
              type: integer
              required: true
        responses:
            200:
                description: Produto deletado com sucesso
            404:
                description: Produto não encontrado
        """
        if produto_services.deletar_produto(id_produto):
            return {"message": "Produto deletado com sucesso!"}, 200
        return {"message": "Produto não encontrado!"}, 404


api.add_resource(ProdutoList, '/produtos')
api.add_resource(ProdutoResource, '/produto/<int:id_produto>')