import MySQLdb
from front_model.front_model import FrameFront

class FrameFrontBD:
    conexao = MySQLdb.connect(host='mysql.padawans.dev', database='padawans19', user='padawans19', passwd='vt2019')
    cursor = conexao.cursor()

    def listar_todos(self):
        comando = f"SELECT * FROM F_FRONTEND_ID"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchall()
        return resultado
    
    def buscar_por_id(self, id):
        comando = f"SELECT * FROM F_FRONTEND_ID WHERE ID = {id}"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchone()
        return resultado

    def salvar(self, frontend:FrameFront):
        comando = f""" INSERT INTO F_FRONTEND_ID
        (
            NOME,
            VERSAO
        )
        VALUES
        (
            '{frontend.nome}',
            '{frontend.versao}'
        )"""
        self.cursor.execute(comando)
        self.conexao.commit()
        id_inserido = self.cursor.lastrowid
        return id_inserido

    def alterar(self, frontend:FrameFront):
        comando = f""" UPDATE F_FRONTEND_ID
        SET
            NOME = '{frontend.nome}'
            VERSAO = '{frontend.versao}'
        WHERE ID = {endereco.id}
        """
        self.cursor.execute(comando)
        self.conexao.commit()

    def deletar(self, id):
        comando = f"DELETE FROM F_FRONTEND_ID WHERE ID = {id}"
        self.cursor.execute(comando)
        self.conexao.commit()