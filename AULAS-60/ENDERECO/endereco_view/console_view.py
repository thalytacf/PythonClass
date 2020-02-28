import sys
sys.path.append('/Users/900163/Desktop/PythonHBSIS/Hard/ENDERECO')
from endereco_controller.endereco_controller import EnderecoController

ec = EnderecoController()

for i in ec.listar_todos():
    print(i)