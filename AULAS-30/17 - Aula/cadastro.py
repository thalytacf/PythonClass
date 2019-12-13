
numero = int(input('Quantidade de cadastros: '))

def cadastro_cliente(numero_funcao):
    dados_clientes = ['codigo_cliente', 'cpf', 'nome_completo', 'data_nasc', 'estado', 'cidade',
                       'cep', 'bairro', 'rua', 'numero_casa', 'complemento']

    lista = []

    for j in rande(numero):
        dicionario = {}

        for i in dados_clientes:
            dicionario[i] = input(f'{i}: ')

        lista.append(dicionario)
    return lista
print(f'Fichas: {cadastro_cliente(numero)}')

#Criar uma função para salvar em arquivo:

# arquivo = open('/Aula17/clientes.txt','a')
# for cliente in arquivo:
#     salvar = f'{cliente['Codigo_cliente']}'
