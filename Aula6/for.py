print ('='*70)

#___Definição de variavel (i) em determinado range
#___Range - intervalo aberto

#___For simples
for i in range (0,10,2):
    print (f'{i} - Eu amo Batata Frita')

print ('='*70)

#___For com incremento de 2
for i in range (0,50,2):
    print (f'{i} - Pares')

print ('='*70)

#___Impressão de lista usando FOR
lista = ['Mateus', 'Matheus', 'Marcela', 'Nicole','Tonho', 'Pablo']
for i in range (0,6):
    print(lista[i])

print ('='*70)

#___Impressão de lista usando FOR - aumeuntando a lista
lista.append('Natan')
for i in range (0,7):
    print(lista[i])

print ('='*70)

#___Impressão de lista usando FOR IT (sem range) - aumeuntando a lista
lista.append('Natan')
for sortudo in  lista:
    print(sortudo)

print ('='*70)

#____For pra resolver a tabuada
numero = 10
for i in range (0,11):
    print (f'{i} x {numero} = {i*numero}')

print ('='*70)