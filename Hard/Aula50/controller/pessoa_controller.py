from flask_restful import Resource
from flask import request

from Hard.Aula50.dao.pessoa_dao import PessoaBD
from Hard.Aula50.model.pessoa_model import Pessoa

class PessoaController(Resource):

    def __init__(self):
        self.dao = PessoaBD()

    def get(self, id=None):
        if id:
            return self.dao.get_by_id(id)
        return self.dao.list_all()


    def post(self):
        nome = request.json['nome']
        sobrenome = request.json['sobrenome']
        idade = request.json['idade']
        pessoa = Pessoa(nome, sobrenome, idade)
        msg = self.dao.insert(pessoa)
        return msg

    def put(self, id):
        nome = request.json['nome']
        sobrenome = request.json['sobrenome']
        idade = request.json['idade']
        pessoa = Pessoa(nome, sobrenome, idade, id)
        msg = self.dao.insert(pessoa)
        msg = self.dao.update('')
        return msg

    def delete(self, id):
        return self.dao.remove(id)