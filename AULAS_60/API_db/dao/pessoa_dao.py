from Hard.Aula50.controller.pessoa_controller import PessoaController
import MySQLdb

from Hard.Aula50.model.pessoa_model import Pessoa
class PessoaBD:
    def __init__(self):
        self.connection = MySQLdb.connect(host='mysql.topskills.dev', database='topskills01', user='topskills01', passwd='ts2019')
        self.cursor = self.connection.cursor()

    def list_all(self):
        self.cursor.execute("SELECT * FROM 01_TCF_PESSOA")
        pessoas = self.cursor.fetchall()
        lista_pessoa = []
        for p in pessoas:
            pessoa = Pessoa(p[1], p[2], p[3], p[0])
            lista_pessoa.append(pessoa.__dict__)
        return lista_pessoa

    def get_by_id(self, id):
        self.cursor.execute("SELECT * FROM 01_TCF_PESSOA WHERE ID = {}".format(id))
        pessoa = self.cursor.fetchone()
        p = Pessoa(pessoa[1], pessoa[2], pessoa[3], pessoa[0])
        return p.__dict__

    def insert(self, pessoa:Pessoa):
        self.cursor.execute("INSERT INTO 01_TCF_PESSOA (NOME, SOBRENOME, IDADE) VALUES ('{}', '{}', '{}')".format(pessoa.nome, pessoa.sobrenome, pessoa.idade))
        self.connection.commit()
        id = self.cursor.lastrowid
        pessoa.id = id
        return

    def update(self, pessoa):
        self.cursor.execute(
            "UPDATE 01_TCF_PESSOA SET NOME = '{}',, SOBRENOME = '{}', IDADE = {}) WHERE ID ={}".format(pessoa.nome,
                                                                                                  pessoa.sobrenome,
                                                                                                  pessoa.idade))

        return 'Alterando a pessoa : {}'.format(pessoa)

    def remove(self, id):
        self.cursor.execute("DELETE FROM 01_TCF_PESSOA WHERE ID = {}".format(id))
        self.connection.commit()
        return 'Removido a pessoa de id : {}'.format(id)