from flask_restful import Api
from flask import Flask

from Hard.Aula51.controller.cerveja_controller import CervejaController


app = Flask(__name__)
api = Api(app)

api.add_resource(CervejaController, '/api/harmony')
#api.add_resource(CervejaController, '/api/harmony<id=int>', endpoint='harm')


@app.route('/')
def home():
    return 'WELCOME // Use the url to continue'


app.run(debug=True, port=80)