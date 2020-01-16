# ===== Classes

# --- Importar biblioteca MySQL
import MySQLdb

def converter_tabela_dicionario(lista_tuplas):
    # --- Configurar a conexao
    conexao = MySQLdb.connect(host='mysql.topskills.study', database='topskills01', user='topskills01', passwd='ts2019')

    # --- Salvar cursor em variavel
    cursor = conexao.cursor()
    # --- Criar dicionario que representa uma pessoa


# --- Criação do comando SQL e passando para o cursor
comando_sql_select = "SELECT * FROM 01_TCF_PESSOA"
cursor.execute(comando_sql_select)


lista_pessoas = []
resultado = cursor.fetchall()
for  p in resultado:
    dic_pessoa = {'id':0, 'nome':'', 'sobrenome':'', 'idade':0, 'endereco_id':0,}
    dic_pessoa['id'= p[0]]
    dic_pessoa['nome'= p[1]]
    dic_pessoa['sobrenome'= p[2]]
    dic_pessoa['idade'= p[3]]
    dic_pessoa['endereco_id'= p[4]]
    lista_pessoas.append(dic_pessoa)


with open('PythonHBSIS/Hard/33 - Aula/pessoas.txt','a') as arquivo:
    for p in lista_pessoas:
        arquivo.write(f"{p['id']};{p['nome']};{p['sobrenome']};{'idade'};{'endereco_id'}\n")


for p in lista_pessoas:
    print(f'\t {p}')
