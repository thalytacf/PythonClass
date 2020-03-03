print('='*70)
menu = '''
==========================================================================================
\t\tI Festival da Cerveija - Itororó')
==========================================================================================
1- Cadastro de Clientes
2- Ver Clientes Cadastrados
3- Cadastro de Produtos
4- Ver Produtos Cadastrados
5- Vendas
6- Relatório de Vendas
7- Sair
Digite a opção desejada:  '''
print('='*70)

opcao= input(menu)

while True: 
    opcao = input(menu)
    if opcao == '1':
        print('Cadastro de Clientes')
    elif opcao == '2':
        print('Ver Clientes Cadastrados') 
    elif opcao == '3':
        print('Cadastro de Produtos')
    elif opcao == '4':
        print('Ver Produtos Cadastrados')
    elif opcao == '5':
        print('Vendas')
    elif opcao == '6':
        print('Relatótio de vendas')
    elif opcao == '7':
        print('Sair')
    else:
        print('Valor Invalido')

######################################################################


