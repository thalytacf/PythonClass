
lista_banda = []
lista_musica = []
lista_album = []
menu = '''
=============================================================================
|                            CADASTRO DE FAIXAS                             |
=============================================================================
1- Cadastro de Banda
2- Cadastro do Album
3- Cadastro da Musica
4- Sair
Digite uma opção: '''



while True:
    opcao = input(menu)
    if opcao == '1':
        lista_banda.append(input('Digite  nome de uma banda: '))
    elif opcao == '2':
        lista_album.append(input('Digite  nome de uma album: '))
    elif opcao == '3':
        lista_musica.append(input('Digite  nome de uma musica: '))
    elif opcao == '4':
        print (f'Lista de banda: {lista_banda} \nLista de album: {lista_album} \nLista de musica: {lista_musica}')
        break                                                                                                                                               
    else: 
        print('Opção Invalida')