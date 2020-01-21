import MySQLdb

class SquadBD:
    conexao = MySQLdb.connect(host='mysql.topskills.study', database='topskills01', user='topskills01', passwd='ts2019')
    cursor = conexao.cursor()

    def listar_todos():
        comando_sql_select = "SELECT * FROM 02_TCF_SQUAD"
        self.cursor.execute(comando_sql_select)
        resultado = self.cursor.fetchall()
        return resultado

    def buscar_por_id(self, id):
        comando = f"SELECT * FROM 02_TCF_SQUAD AS S WHERE S.ID = {id}"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchone()
        return resultado

    def salvar(self, squad:Squad):
        comando = f""" INSERT INTO 02_TCF_SQUAD
        (
            NOME,
            DESCRICAO,
            NUMEROPESSOAS,
            LINGUAGEMBACKEND,
            FRAMEWORKFRONTEND
        )
        VALUES
        (
            '{squad.nome}',
            '{squad.descricao}',
            {squad.numpessoas},
            {squad.backend},
            {squad.frontend}
        )"""
        self.cursor.execute(comando)
        self.conexao.commit()
        id_inserido = self.cursor.lastrowid
        return id_inserido

    def alterar(self, squad:Squad):
        comando = f""" UPDATE 02_TCF_SQUAD
        SET
            NOME = '{squad.nome}',
            DESCRICAO ='{squad.descricao}',
            NUMEROPESSOAS = {squad.numpessoas},
            LINGUAGEMBACKEND = {squad.backend}
            FRAMEWORKFRONTEND = {squad.frontend}
        WHERE ID = {squad.id}
        """
        self.cursor.execute(comando)
        self.conexao.commit()

    def deletar(self, id):
        comando = f"DELETE FROM 02_TCF_SQUAD WHERE ID = {id}"
        self.cursor.execute(comando)
        self.conexao.commit()