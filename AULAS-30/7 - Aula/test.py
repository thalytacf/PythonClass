# dicionario_bandas ={'Nome':''}
# dicionario_bandas['Nome'] = Calipso
# dicionario_bandas['Nome'] = Dejavu

# print (dicionario_bandas)

# dicionario = {'Nome':'Thalyta', 'Sobrenome':'Ficher'}
# dicionario['Sobrenome'] = Lima
# dicionario['CPF'] = '333.555.999-11'


dicionario_dados = {'nome':'', 'cpf':'', 'rg':''}
lista_pessoas = []
for i in range (1,11):
    dicionario_dados['nome'] = input ('Nome: ')
    dicionario_dados['cpf'] = input ('CPF: ')
    dicionario_dados['rg'] = input ('RG: ')
    lista_pessoas.append (dicionario_dados)
for dicionario_dados in lista_pessoas:
    print (lista_pessoas)