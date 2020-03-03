from flask_restful import Resource


class PessoaController(Resource):
    def get(self):
        return 'Pessoa via GET'

    def put(self):
        return 'Pessoa via PUT'

    def post(self):
        return 'Pessoa via POST'

    def delete(self):
        return 'Pessoa via DELETE'