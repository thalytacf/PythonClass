from dao.squad_dao import SquadBD
from model.squad_model import Squad

class SquadController:
    dao = SquadBD()

    def listar_todos(self):
        lista_squads = []
        lista_tuplas = self.dao.listar_todos()
        for x in lista_tuplas:
            squad = Squad()
            squad.id =  x[0]
            squad.nome = x[1]
            squad.descricao = x[2]
            squad.numpessoas = x[3]
            squad.backend = x[4]
            squad.frontend = x[5]
            lista_squads.append(squad)
        return lista_squads

    def buscar_por_id(self, id):
        x = self.dao.buscar_por_id(id)
        squad = Squad()
        squad.id =  x[0]
        squad.nome = x[1]
        squad.descricao = x[2]
        squad.numpessoas = x[3]
        squad.backend = x[4]
        squad.frontend = x[5]
        return squad

    def salvar(self, squad:Squad):
        return self.dao.salvar(squad)

    def alterar(self, squad:Squad):
        return self.dao.alterar(squad)

    def deletar(self, id):
        return self.dao.deletar(id)