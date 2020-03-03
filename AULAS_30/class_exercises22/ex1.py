# Crie uma classe cliente:

# 1) deve ter como atributos: codigo, cpf, nome, idade, sexo

# 2) como metodos: receber salario, comprar, pagar divida

# Quando recebe aumenta o dinheiro na carteira.

# quando compra aumenta os bens e diminui o dinheiro na carteira

# Se comprar e não tiver dinheiro o suficiente deve diminuir o dinheiro da carteira
# e aumentar a divida.

# Para pagar a divida tem que ter dinheiro o suficiente na carteira

# 3) atributos de estado: dinheiro na carteira, divida, bens


###Atributos
cpf
codigo
nome
idade
sexo

###Metodos
receber
comprar
pagar

###Atributos de estado
dinheiro na carteira
divida
bens

class Pessoa:
    '''
    Esta classe é uma demonstração para aula
    '''
    def __init__ (self, cpf1, codigo1, nome1, idade1, sexo1):
        ''' 
        O __init__ é o motor que irá iniciar as variáveis da clase
        O self é o que irá conecta toda a classe
        '''
        # Atributos ##########
        self.cpf = cpf1
        self.codigo = codigo1
        self.nome = nome1
        self.idade = idade1
        self.sexo = sexo1
        # 
        self.divida = None
        self.din_carteira= 'não'
        self.bens= 'não'
        
    #### Metodos

    def receber (self,respirar):
        if self.receber = 1 or self.receber = <1:
            self.din_carteira = self.receber

    def comprar (self,valor):
        if self.comprar:
            self.din_carteira = self.din_carteira - 1
            self.bens = self.bens + 1

    def pagar (self):
       
p = Pessoa('00000000000', 'abc','Thalyta',19,'f')

p.receber()
p.comprar()
p.pagar()

print(f'Nome é {p.nome}')
print(f'Total de dinheiro: R$ {p.din_carteira}')
print(f'Total de bens: {p.bens}')
print(f'Divida total: {p.divida}')