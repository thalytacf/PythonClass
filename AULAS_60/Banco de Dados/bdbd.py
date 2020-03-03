#pip3 

import MySQLdb

# conexao = MySQLdb.connect(host='mysql.topskills.study', database='topskills01', user='topskills01', passwd='ts2019')

# cursor= conexao.cursor()
# cursor.execute('SELECT * FROM THALYTA')
# pessoas= cursor.fetchall()
# for p in pessoas:
#     print(p)
#######LOCAL
# conexao = MySQLdb.connect(host='127.0.0.1:3306', database='auladb', user='root', passwd='')
# cursor= conexao.cursor()
# cursor.execute('SELECT * FROM pessoa')
# pessoas= cursor.fetchall()
# for p in pessoas:
#     print(p)

conexao = MySQLdb.connect(host='mysql.topskills.study', database='topskills01', user='topskills01', passwd='ts2019')
cursor= conexao.cursor()

def listar_todos(c):
    c.execute('SELECT * FROM THALYTA')
    pessoas= cursor.fetchall()
    for p in pessoas:
        print(p)

def buscar_id(c, id):
    c.execute(f'SELECT * FROM THALYTA WHERE ID = {id}')
    pessoa = c.fetchone()
    print(pessoa)

listar_todos(cursor)
print('-'*70)
buscar_id(cursor, 2)
print('-'*70)