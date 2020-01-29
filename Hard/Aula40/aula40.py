from flask import Flask
from flask_restful import Api
from Hard.Aula40.Controller.cerveja_controller import CervejaCrontoller
#GET
#POST
#PUT-
#DELETE

app = Flask(__name__)
api = Api(app)
api.add_resource(CervejaCrontoller, '/api/cerveja')


@app.route('/')
def home():
    return 'WELCOME to API'


app.run(debug=True, port=80)