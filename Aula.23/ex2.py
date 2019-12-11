# Como Tratar e Trabalhar Erros!!!

# Com base no seguinte dado bruto:

# 1) Faça uma classe cliente que receba como parametro o dado bruto.
# 2) A classe deve iniciar (__init__) guardando o dado bruto nume variável chamada self.dado_bruto
# 3) As variáveis  código cliente (inteiro), nome, idade (inteiro), sexo, email, telefone
# devem iniciar com o valor None
# 4) Crie um metodo que pegue o valor bruto e adicione nas variáveis:
# código cliente (inteiro), nome, idade (inteiro), sexo, email, telefone
# convertendo os valores de string para inteiros quando necessários. 
# (Faça da forma que vocês conseguirem! O importante é o resultado e não como chegaram nele!)
# 5) Crie um metodo salvar que pegue os seguintes dados do cliente e salve em um arquivo. 
# código cliente (inteiro), nome, idade (inteiro), sexo, email, telefone
# 6) crie um metodo que possa atualizar os dados do cliente (código cliente (inteiro), 
# nome, idade (inteiro), sexo, email, telefone). Este metodo deverá alterar tambem 
# o dado bruto para que na hora de salvar o dado num arquivo, o mesmo não estaja desatualizado.

class Pessoa:
    '''
    Classe de Pessoa
    '''
    def __init__ (self, dadobruto):
        self.dado_bruto = dadobruto
        self.codigo = None
        self.nome = None
        self.idade = None
        self.sexo = None
        self.email = None
        self.telefone = None
        self.sexo = None

    def tratar_dados(self):
        pessoa = self.dado_bruto.strip().split(';')
        self.codigo = int(pessoa[0])
        self.nome = pessoa[1]
        self.idade = int(pessoa[2])
        self.sexo = pessoa[3]
        self.email = pessoa[4]
        self.telefone = pessoa[5]

    def salvar (self):
        arquivo = open('PythonHBSIS/Aula.23/Pessoa.txt','a')
        arquivo.write(f'{self.codigo};{self.nome};{self.idade};{self.sexo};{self.email};{self.telefone}\n')
        arquivo.close()

    #def update ()
        #Lista????

dadobruto = '1;Arnaldo;23;m;alexcabeludo2@hotmail.com;014908648117'
pess = Pessoa(dadobruto)
pess.salvar()
pess.tratar_dados()

#arquivo.write(f'{self.codigo};{self.nome};{self.idade};{self.sexo};{self.email};{self.telefone}\n')
#arquivo.write(f'{pessoa[0]};{pessoa[1]};{pessoa[2]};{pessoa[3]};{pessoa[4]};{pessoa[5]}\n')