from flask_restful import Resource
from flask import request,jsonify,make_response
from src.schemas.user_schema import (usuario_schema, usuario_schema)
from marshmallow import ValidationError
from src.services import user_services

class UsuarioList(Resource):
    def get(self):

        """
        Lista todos os usuários
        ---

        tags:
          - Usuários
        responses:
          200:
             descripition: Lista de Usuários
          400:
             descripition: Nenhum usuário encontrado
        """

        usuarios = user_services.listar_usuario()
        if not usuarios:
            return make_response(jsonify({'message':'Não existem usuarios!'}),404)
        return make_response(jsonify(usuario_schema.dump(usuarios)),200)
    def post(self):

        """
        Cadastrar um novo usuário 
        ---
        tags:
          -- Usuários
        parameters:
         - in: body
           name: body
           required: True
           schema:
             type:object
             properties:
                 nome:
                    type:string
                    example:Karython Gomes
                email:
                    type:string
                    example: gomes@gmail.com
                senha:
                   type:string
                   example:senha123
        responses:
         201:
           description: Usuario cadastrado
         400:
           descripition: Erro de validação
         409:
           descripition: Email já cadastrado 
        """



        try:
            usuario = usuario_schema.load(request.get_json())
        except ValidationError as err:
            return err.messages, 400

        if user_services.listar_usuario_email(usuario.email):
            return {'message':'email ja cadastrado'}, 409
        
        try:
            resultado = user_services.cadastrar_usuario(usuario)

            return usuario_schema.dump(resultado),201
        except Exception as e:
            return {
                "message":str(e)
            }, 400

api.add_resource(UsuarioList, '/usuarios')

class UsuarioResource(Resource):
    def get(self,id_usuario):

        """
        Buscar usuário por ID
        ---
        tags:
         - Usuários
        parameters:
         - name: id_usuario
           in: path
           type: integer
           required: True
        responses:
          200:
            descripition: Lista de Usuários
          404:
            descripition: Nenhum usuário encontrado
        """




        usuario = user_services.listar_usuario_id(id_usuario)
        if not usuario:
            return {
                'message' : 'Usuario nao encontrado!'
            },404
        return usuario_schema.dump(usuario), 200
    def put(self,id_usuario):

        
        """
        Cadastrar um novo usuário 
        ---
        tags:
          -- Usuários
        parameters:
          - name: id_usuario
            in: path
            type: integer
            required: True
          - in: body
            name: body
            required: True
            schema:
              type: object
              properties:
                nome:
                  type:string
                email:
                  type:string
                senha:
                  type:string
        responses:
          201:
           description: Usuario cadastrado
          400:
             descripition: Erro de validação
          409:
             descripition: Email já cadastrado 
        """

        try:
            novo_usuario = usuario_schema.load(request.get_json())
        except ValidationError as err:
            return err.messages, 400
        usuario = user_services.editar_usuario(
            id_usuario,{
                'nome':novo_usuario.nome,
                'email':novo_usuario.email,
                'senha':novo_usuario.senha
            }
        )
        if not usuario:
            return{'message': "Usuario nao encontrado"},404
        
        return usuario_schema.dump(usuario),200
    def delete(self, id_usuario):
        """
        Deletar Usuário
        ---
        tags:
         - Usuário
        parameters:
         - name: id_usuario
           in: path
           type: integer
           required: True
        response:
          200:
            descripition: Usuário removido
          404:
           descripition: Nenhum usuário encontrado
        """
        if user_services.deletar_usuario(id_usuario):
            return{
                'message' : 'Usuario deletado com sucesso!'
            },200
        return usuario_schema.dump(usuario),200
api.add_resource(UsuarioResource, '/usuarios/<int:id_usuario>')
