from flask import Flask, render_template, request, redirect
import sys
sys.path.append('/Users/900163/Desktop/git/PythonHBSIS/Hard/37 - Aula')
from controller.squad_controller import SquadController
from model.squad_model import Squad

app = Flask(__name__)
squad_controller = SquadController()
nome = 'Cadastro de Squads'

@app.route('/')
def inicio():
    return render_template('homepage.html', titulo_app = nome)

@app.route('/listarfront')
def listar():
    squads = squad_controller.listar_todos()
    return render_template('listarfront.html', titulo_app = nome, lista = squads)
    
@app.route('/listarback')
def listar():
    squads = squad_controller.listar_todos()
    return render_template('listarback.html', titulo_app = nome, lista = squads)

@app.route('/listarsgbds')
def listar():
    squads = squad_controller.listar_todos()
    return render_template('listarsgbds.html', titulo_app = nome, lista = squads)

@app.route('/listar')
def listar():
    squads = squad_controller.listar_todos()
    return render_template('listar.html', titulo_app = nome, lista = squads)

@app.route('/cadastrarsquads')
def cadastrar():
    squad = Squad()
    if 'id' in request.args:
        id = request.args['id']
        squad = squad_controller.buscar_por_id(id)
    return render_template('cadastrar.html', titulo_app = nome, pessoa = squad)


@app.route('/excluir')
def excluir():
    id = int(request.args['id'])
    squad_controller.deletar(id)
    return redirect('/listar')

@app.route('/salvar')
def salvar():
    squad = Squad()
    squad.id = int(request.args['id'])
    squad.nome = request.args['nome']
    squad.descricao = request.args['descricao']
    squad.numpessoas = request.args['numpessoas']
    squad.backend = request.args['backend']
    squad.frontend = request.args['frontend']
    
    if squad.id == 0:
        squad_controller.salvar(squad)
    else:
        squad_controller.alterar(squad)
    return redirect('/listar')

app.run(debug=True)