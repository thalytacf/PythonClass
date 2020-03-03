#___Estrutura de decisoes

listanum = []
num = 5

if 'Thalyta'.count('a') > 0:
    print ('Existe')

if 'a' in 'Thalyta':
    print ('Existe')

if 'j' not in 'Thalyta':
    print ('Nao existe')
if num in listanum:
    print ('Existe')
else:
    print ('Nao existe')

lista_vazia = []

if len(lista_vazia) == 0:
    print ('Vazia')
else:
    print ("Não vazia")

lista_nomes = []

if lista_nomes:
    print('Tem nomes')
else:
    print('Não tem nomes')

nome = ''
print(nome)
nome = 'Thalyta'
print(nome[3])

#___String é imutavel
#nome[2] = 'o'
#print(nome)

if nome:
    print('Preenchido')
else:
    print('Vazio')

