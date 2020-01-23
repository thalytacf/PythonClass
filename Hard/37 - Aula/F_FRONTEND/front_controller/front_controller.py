from front_dao.front_dao import FrameFrontBD
from front_model.front_model import FrameFront

class FrameFrontController:
    dao = FrameFrontBD()

    def listar_todos(self):
        return self.dao.listar_todos()

    def buscar_por_id(self, id):
        return self.dao.buscar_por_id(id)

    def salvar(self, frontend:FrameFront):
        return self.dao.salvar(frontend)

    def alterar(self, frontend:FrameFront):
        self.dao.alterar(frontend)

    def deletar(self, id):
        self.dao.deletar(id)