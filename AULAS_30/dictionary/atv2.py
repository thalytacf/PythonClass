# ler 11 jogadores
# Jogador: nome, posicao, numero,pernaboa
# crie m dicionario para armazenaros dados
# imprimmir tudo

dicionario_dados = {'nome':'', 'posicao':'', 'numero':'', 'pernaboa':''}
lista = []
for i in range (1,3):
    dicionario_dados['nome'] = input ('Nome: ')
    dicionario_dados['posicao'] = input ('Posição: ')
    dicionario_dados['numero'] = int(input ('Numero: '))
    dicionario_dados['pernaboa'] = input ('Perna Boa: ')
    lista.append (dicionario_dados)
print(lista)