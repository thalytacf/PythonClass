import sys
sys.path.append('/Users/900163/Desktop/git/PythonHBSIS/Hard/37 - Aula')
from controller.squad_controller import SquadController
from model.squad_model import Squad


squad = Squad()
squad.nome = ''
squad.descricao = ''
squad.numpessoas = ''
squad.backend = ''
squad.frontend = ''

controller = SquadController()
id_salvo = controller.salvar(squad)
print(controller.buscar_por_id(1))