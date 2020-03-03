from flask import Flask
from flask_restful import Api


from Hard.AulaX.controller.perfil_controller import PerfilController

app = Flask(__name__)
api = Api(app)

api.add_resource(PerfilController, '/api/perfil',endpoint='perfis')
api.add_resource(PerfilController, '/api/perfil/<int:id>',endpoint='perfil'0)

app.run(debug=True, port=80)

