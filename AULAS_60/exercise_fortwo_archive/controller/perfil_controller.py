from flask_restful import Resource

from Hard.AulaX.dao.perfil_dao import PerfilDao

class PerfilController(Resource):
    def __init__(self):
        self.dao = PerfilDao()

    def get(self, id=None):
        if id:
            return self.dao.get_by_id(id)
        return self.dao.list_all()