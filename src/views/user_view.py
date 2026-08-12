from flask_restful import Resource
from flask import request,jsonify,make_response
from src.schemas.user_schema import (usuario_schema, usuario_schema)
from marshmallow import ValidationError
from src.services import user_services

class UsuarioList(Resource):
    def get(self):
        usuarios = user_services.listar_usuario()
        if not usuarios:
            return make_response(jsonify({'message':'Não existem usuarios!'}),404)
        return make_response(jsonify(usuario_schema.dump(usuarios)),200)
    def post(self):
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
        usuario = user_services.listar_usuario_id(id_usuario)
        if not usuario:
            return {
                'message' : 'Usuario nao encontrado!'
            },404
        return usuario_schema.dump(usuario), 200
    def put(self,id_usuario):
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
        if user_services.deletar_usuario(id_usuario):
            return{
                'message' : 'Usuario deletado com sucesso!'
            },200
        return usuario_schema.dump(usuario),200
api.add_resource(UsuarioResource, '/usuarios/<int:id_usuario>')
