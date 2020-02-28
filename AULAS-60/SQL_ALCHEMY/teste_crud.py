import sqlalchemy as db
from sqlalchemy.orm.session import sessionmaker


# ---------- Aqui definimos a conexão -----------

conexao = db.create_engine("mysql+mysqlconnector://root:@localhost:3306/test")
criador_sessao = db.orm.sessionmaker()
criador_sessao.configure(bind=conexao)
sessao = criador_sessao()


# ----- INSERIR DADOS -------

nome = input("Digite nome: ")
sobrenome = input("Digite sobrenome: ")
idade= int(input("Digite idade: "))

conexao.execute(f"insert into pessoas (nome, sobrenome, idade) values ('{nome}','{sobrenome}',{idade})")

# ----- LISTAR DADOS -------

def listar():
    query = conexao.execute("select * from pessoas")
    lista = [q for q in query]
    return lista

# ----- DELETAR DADOS -------

id = int(input("Digite o id que deseja deletar:  "))

conexao.execute(f"DELETE FROM pessoas WHERE id={id}")


# ----- ALTERAR DADOS -------

id = int(input("Digite o id que deseja alterar: "))
nome = input("Digite nome: ")
sobrenome = input("Digite sobrenome: ")
idade= int(input("Digite idade: "))

conexao.execute(f"UPDATE pessoas SET nome='{nome}', sobrenome='{sobrenome}', idade={idade} WHERE id={id}")
