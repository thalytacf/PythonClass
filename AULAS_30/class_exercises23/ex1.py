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

    # def __str__ (self):
    #     texto = f'''   
    #     Codigo = {self.codigo}
    #     Nome = {self.nome}
    #     Idade = {self.idade} 
    #     Sexo = {self.sexo}
    #     Email = {self.email}
    #     Telefone = {self.telefone} 
    #     Sexo = {self.sexo} 
    #     '''
    #    return texto

    def tratar_dados(self):
        pessoa = self.dado_bruto.strip().split(';')
        self.codigo = int(pessoa[0])
        self.nome = pessoa[1]
        self.idade = int(pessoa[2])
        self.sexo = pessoa[3]
        self.email = pessoa[4]
        self.telefone = pessoa[5]
        

dadobruto = '1;Arnaldo;23;m;alexcabeludo2@hotmail.com;014908648117'
#pess = []
pess = Pessoa(dadobruto)
#pess[0].tratar_dados()

print (f'Codigo:{pess.codigo} \nNome: {pess.nome}')
#print(pess[0])
# def recebeValor (self, dado_bruto):
# self.codigo = dado_bruto[0]
# self.nome = dado_bruto[1]
# self.idade = dado_bruto[2]
# self.sexo = dado_bruto[3]
# self.email = dado_bruto[4]
# self.telefone = dado_bruto[5]


