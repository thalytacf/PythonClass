from flask import Flask
from flask_restful import Api

from Hard.Aula50.controller.pessoa_controller import PessoaController

app = Flask(__name__)
api = Api(app)
api.add_resource(PessoaController, '/api/pessoa', endpoint='pessoas')
api.add_resource(PessoaController, '/api/pessoa/<id:int>', endpoint='pessoa')

@app.route('/')
def homepage():
    return "Welcome, sit&wait"


app.run(debug=True, port=80)