print("="*70)
#___Inicialização de uma variável lista
lista1 = []
#___Inicialização de uma variável lista, com elementos
lista2 = ['Marcela','Nicole', 'Matheus']
#___Lista com inteiros
lista3 = [1,2,3,4,5]
#___Impressão das listas
print(lista1)
print(lista2)
print(lista3)
#___Adicionando elementos em uma lista já criada
lista1.append(lista2)
lista1.append(lista3)
print(lista1)
#___Criação de lista com dados lidos
listaperg = [input('Digite seu cantor favorito:'), input('Digite seu pianista favorito:')]
#___Recuperando um dado de uma posição especifica da lista
posicao = int (input('Digite a posição:'))
print(lista2[posicao-1])

print("="*70)