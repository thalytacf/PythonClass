# Crie uma classe cliente:

# 1) deve ter como atributos: codigo, cpf, nome, idade, sexo
class Pessoas:
   def __init__(self, codigo, cpf, nome, idade, sexo):
        self.codigo = codigo
        self.cpf =cpf
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
    def action(self,receber salario, comprar, pagar divida)


# 2) como metodos: receber salario, comprar, pagar divida



# Quando recebe aumenta o dinheiro na carteira.

# quando compra aumenta os bens e diminui o dinheiro na carteira

# Se comprar e não tiver dinheiro o suficiente deve diminuir o dinheiro da carteira
# e aumentar a divida.

# Para pagar a divida tem que ter dinheiro o suficiente na carteira

# 3) atributos de estado: dinheiro na carteira, divida, bens
