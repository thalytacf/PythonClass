#----- Importar biblioteca do Mysql
import MySQLdb
from model.backend import BackEnd


class BackEndDao:

    def __init__(self):
        #----- Configurar a conexão
        self.conexao = MySQLdb.connect(host='mysql.padawans.dev', database='padawans19', user='padawans19', passwd='vt2019')
        #----- Salva o cursor da conexão em uma variável
        self.cursor = self.conexao.cursor()

    def listar_todos(self):
        #----- Criação do comando SQL e passado para o cursor
        comando_sql_select = "SELECT * FROM BACKEND"
        self.cursor.execute(comando_sql_select)
        #---- Pega todos os resultados da execução do comando SQL e armazena em uma variável
        resultado = self.cursor.fetchall()
        return resultado

    def buscar_por_squad(self, id):
        comando = f"""
                SELECT 
                B.NOME 
                FROM RELACIONAMENTO AS R
                JOIN BACKEND AS B
                ON R.BACK_ID = B.ID
                JOIN SQUADS AS S
                ON R.SQUAD_ID = S.ID
                WHERE S.ID = {id}"""
        self.cursor.execute(comando)
        resultado = self.cursor.fetchall()
        return resultado

    def buscar_por_id(self, id):
        #----- Criação do comando SQL e passado para o cursor
        comando = f"SELECT * FROM BACKEND WHERE ID = {id}"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchone()
        return resultado

    def salvar(self, backend: BackEnd):
        comando = f" INSERT INTO BACKEND(NOME,VERSAO)VALUES('{backend.nome}','{backend.versao}')"
        self.cursor.execute(comando)
        self.conexao.commit()
        id_inserido = self.cursor.lastrowid
        return id_inserido
    
    def alterar(self, backend: BackEnd):
        comando = f" UPDATE BACKEND SET NOME = '{backend.nome}', VERSAO = '{backend.versao}' WHERE ID = {backend.id}"
        self.cursor.execute(comando)
        self.conexao.commit()
    
    def deletar(self, id):
        comando4 = f"DELETE FROM RELACIONAMENTO WHERE BACK_ID = {id}"
        self.cursor.execute(comando4)
        self.conexao.commit()
        comando = f"DELETE FROM BACKEND WHERE ID = {id}"
        self.cursor.execute(comando)
        self.conexao.commit()