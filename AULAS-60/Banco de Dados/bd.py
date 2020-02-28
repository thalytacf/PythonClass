from flask_mysql importMySQLdb
from contextlib import closing

__daos = {'host': "mysql.topskills.study",
            'database':"topskiils01",
            'user': "topskiils01",
            'passwd':"ts2019",
            'port':3306}

def cadastrar (cerveja, prato):
    with closing(MySQLdb.connect(**__dados)) as conn
        cursor = conn.cursor()
        cursor.execute(f"INSERT INTO topskills01 Thalyta (CERVEJA, PRATO) VALUES ('{cerveja}','{prato}');")
        conn.commit()

def consultarAll():
    with closing(MySQLdb.connect(**__dados)) as conn
        cursor = conn.cursor()
        cursor.execute('SELECT *FROM Thalyta')
        print('\nSó uma linha',cursor.fetchone())
        print('\nVarias linhas'),cursor.fetchall())

for i in range (5):
    cerveja = input('Cerveja: ')
    prato = input('Prato: ')
    cadastrar(cerveja,prato)

consultarAll()


# SELECT * FROM thalyta_PESSOA AS P
# JOIN thalyta_ENDERECO AS E
# ON P.ENDERECO_ID = E.ID

SELECT NOME, IDADE FROM pessoa;
INSERT INTO pessoa (LOGRADOURO, NUMERO, COMPLEMENTO, BAIRRO, CIDADE)
VALUES ('Rua Barra Velha', 54, 'segunda casa', 'Santa Terezinha', 'Gaspar');

# INSERT INTO `aulabd`.`endereco` (`RUA`, `NUMERO`, `BAIRRO`) VALUES ('Barra Velha', '54', 'Santa Terezinha');
# INSERT INTO `aulabd`.`endereco` (`RUA`, `NUMERO`, `BAIRRO`) VALUES ('Maria Campestrini', '45', 'Vila Nova');
