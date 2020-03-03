from flask import Flask, render_template
import sys
sys.path.append('/Users/900163/Desktop/PythonHBSIS/Hard/ENDERECO')
from endereco_controller.endereco_controller import EnderecoController

app = Flask(__name__)
ec = EnderecoController()

@app.route('/')
def inicio():
    endereco = ec.listar_todos()
    return render_template('index.html', lista = endereco)

app.run()