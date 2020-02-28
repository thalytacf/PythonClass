# -- Importando a classe principal do alchemy
import sqlalchemy as db

#-- Criando classe que representa a nossa conexão e sessão, (acessa o nosso banco de dados)
class BaseDao:
    #-- declarando o método construtor que define as conf para acesso ao banco de dados
    def __init__(self):
        # -- cirar engine e passar a configuração de acesso ao DATABASE
        connection = db.create_engine("mysql+mysqlconnector://root:@localhost/test")
        # -- Criar uma variável que define nossa sessão ao DataBase
        criar_sessao = db.orm.sessionmaker()
        # Configurando a nossa conexão
        criar_sessao.configure(bind=connection)
        self.sessao = criar_sessao()