import sys
sys.path.append('Users/900163/Desktop/git/PythonHBSIS/Hard/37 - Aula')
from front_controller.front_controller import FrameFrontController
from front_model.front_model import FrameFront

front = FrameFront()
front.nome = 'Teste'
front.versao = 'Teste'

contr=  FrameFrontController()
id_salvo = contr.salvar(front)
print(contr.buscar_por_id(id_salvo))