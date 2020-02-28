
from Hard.Aula41.Controller.start import PessoaController
from flask import Flask
from flask_restful import Api

app = Flask(__name__)
api = Api(app)
api.add_resource(PessoaController, '/api/pessoa')


@app.route('/')
def inicio():
    return 'Welcome - Sit&Wait'


app.run(debug=True, port=80)