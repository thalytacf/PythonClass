# vari = input('whatever: ')
# arquivo = open('Aulas15.txt','a')

# arquivo.write(f'{vari}\n')


# # for linha in arquivo:
# #     print(linha)


# arquivo.close()

#Aula 15 - Manipulação de arquivos
# vari = input('whatever: ')

def safe_people (people_dic):
  arquivo = open('Aulas15.txt', 'a')
  arquivo.write(f"{people_dic['nome']};{people_dic['sobrenome']};{people_dic['idade']}  \n")
  arquivo.close()

def read ():
    lista = []
    arquivo = open('Aulas15.txt', 'r')
    for linha in arquivo:
        linha = linha.strip()
        lista_linha = linha.split(';')
        pessoa = {'nome':lista_linha[0], 'sobrenome':lista_linha[1] , 'idade': lista_linha[2]}
        # print(lista_linha)
        # lista.append(linha)
        lista.append(pessoa)
    arquivo.close()
    return lista


nome = input('Digite nome:')
sobrenome = input('Digite sobrenome:')
idade = int(input('Digite idade:'))

pessoa = {'nome':nome, 'sobrenome': sobrenome, 'idade': idade}
safe_people(pessoa)
# print (read())

# for linha in arquivo:
#     print(linha)

lista = ler ()

for p in lista:
  print(f"{p['nome']} - {p - ['sobrenome']} - {p['idade']}")