import MySQLdb

from Hard.Aula51.model.cerveja_model import Cerveja

class CervejaBD():
    def __init__(self):
        self.connection = MySQLdb.connect(host='mysql.topskills.dev', database='topskills01', user='topskills01', passwd='ts2019')
        self.cursor = self.connection.cursor()

    def list_all(self):
        self.cursor.execute("SELECT * FROM THALYTA")
        harmony = self.cursor.fetchall()
        lista_harmonizacao = []
        for i in harmony:
            harm = Cerveja(i[1], i[2], i[3], i[0])
            lista_harmonizacao.append(harm.__dict__)
        return lista_harmonizacao

    def get_by_id(self, id):
        self.cursor.execute("SELECT * FROM THALYTA WHERE ID = {}".format(id))
        harm = self.cursor.fetchone()
        h = Cerveja(harm[1], harm[2], harm[3], harm[0])
        return h.__dict__


    def insert(self, harmony:Cerveja):
        self.cursor.execute("INSERT INTO THALYTA (CERVEJA, PRATO, OCASIAO) VALUES('{}','{}',{})".format(harmony.cerveja, harmony.prato, harmony.ocasiao))
        self.connection.commit()
        id = self.cursor.lastrowid
        harmony.id = id
        return harmony.__dict__)

    def update(self, harmony:Cerveja):
        self.cursor.execute(" UPDATE THALYTA SET  CERVEJA = '{}', PRATO = '{}', OCASIAO = {} WHERE ID = {}".format(harmony.cerveja, harmony.prato, harmony.ocasiao, harmony.id))
        self.connection.commit()
        return harmony.__dict__

    def remove(self):
        self.cursor.execute("DELETE FROM THALYTA WHERE ID = {}".format(id))
        self.cursor.commit()
        return 'Removido harminização de id : {}'.format(id)
