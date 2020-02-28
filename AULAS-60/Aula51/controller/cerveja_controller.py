from flask_restful import Resource
from flask import request

from Hard.Aula51.dao.cerveja_dao import CervejaBD
from Hard.Aula51.model.cerveja_model import Cerveja


class CervejaController(Resource):

    def __init__(self):
        self.dao = CervejaBD()

    def get(self, id=None):
        if id:
            return self.dao.get_by_id(id)
        return self.dao.list_all()

    def put(self, id):
        cerveja = request.json['cerveja']
        prato = request.json['prato']
        ocasiao = int(request.json['ocasiao'])
        harmony = Cerveja(cerveja, prato, ocasiao, id)
        msg = self.dao.update(harmony)
        return msg

    def post(self):
        cerveja = request.json['cerveja']
        prato = request.json['prato']
        ocasiao = int(request.json['ocasiao'])
        harmony = Cerveja(cerveja, prato, ocasiao, id)
        msg = self.dao.insert(harmony)
        return msg

    def delete(self, id):
        return self.dao.remove(id)
