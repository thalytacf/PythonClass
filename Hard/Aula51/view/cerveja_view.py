from flask_restful import Api
from flask import Flask

from Hard.Aula51.controller.cerveja_controller import PessoaController


app = Flask(__name__)
api = Api(app)

api.add_resource(PessoaController, '/api/harmony')
api.add_resource(PessoaController, '/api/harm')

@app.route('/')
def home():
    return 'WELCOME // Use the url to continue'


 app.run(debug=True, port=80)