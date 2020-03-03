# Aula 21 - 16-12-2019
#Funções para listas

from geradorlista import lista_simples_int
from random import randint

lista1 = lista_simples_int(randint(5,100))
lista2 = lista_simples_int(randint(5,75))
lista3 = lista_simples_int(randint(5,70))

# lista1 = [2,3,4,5]
# lista2 = [6,7,8,9]

# 1) Com as listas aleatórias (lista1,lista2,lista3) e usando as funções para listas,
# f-string, responda as seguintes questões:

print('='*70)

# 1.1) Qual é o tamanho da lista1?
print(f'O tamanho da lista1 é de {len(lista1)} iten(s)')

# 1.2) Qual é o maior valor da lista2?
print(f'O maior valor da lista2 é {max(lista2)}')

# 1.3) Qual seria a soma do maior valor com o menor valor da lista2?

print(f'Soma = {(max(lista2))+(min(lista1))}')

# 1.4) Qual é a média aritmética da lista1?
print(f'Media lista1 = {(sum(lista1))/(len(lista1))}')

# 1.5) Qual o valor da soma de todas as listas e a soma total delas?
# quero que mostre a soma individual (por lista) e a soma total de todas elas (soma das somas das listas)
soma1 = sum(lista1)
soma2 = sum(lista2)
soma3 = sum(lista3)
lista_soma = [soma1,soma2]
print('*'*50)
print(f'Soma das listas = {sum(lista_soma)}')
# 1.6) Usando o f-string, imprima todos os valores da lista1 um de baixo do outro.
print('*'*50)
n = 0
for elemento in lista1:
    print(f'{n}- {elemento}\n')
    n = n + 1

# 1.7) Com a indexação e f-string, mostre o valor das posições 5, 9, 10 e 25 de cada lista.
# trate para evitar o erro: IndexError
print('*'*50)
try:
    print(f'Lista1 \n\t5- {lista1[5]} \n\t9- {lista1[9]} \n\t10- {lista1[10]} \n\t25- {lista1[25]}')
    print(f'Lista2 \n\t5- {lista2[5]} \n\t9- {lista2[9]} \n\t10- {lista2[10]} \n\t25- {lista2[25]}')
    print(f'Lista3 \n\t5- {lista3[5]} \n\t9- {lista3[9]} \n\t10- {lista3[10]} \n\t25- {lista3[25]}')
except:
    pass
# 1.8) Mostre qual das listas tem mais itens (lembre-se, as listas são randômicas, não há como prever o 
# tamanho delas).
count1 = (len(lista1))
count2 = (len(lista2))
count3 = (len(lista3))
print ('*'*50)
if (count1>count2 and count1>count3):
    print(F'A lista1 é a maior')
elif (count2>count1 and count2>count3):
    print(F'A lista2 é a maior')
elif (count3>count2 and count3>count1):
    print(F'A lista3 é a maior')

# 1.9) Some os maiores números de todas as listas e subtraia pelo menor número dos menores valores das listas.
# Para obter o menor valor, pegue o menor valor das listas e veja qual deles é o menor e use ele.
maxi1 = (max(lista1))
maxi2 = (max(lista2))
maxi3 = (max(lista3))
mini1 = (min(lista1))
mini2 = (min(lista2))
mini3 = (min(lista3))
if (mini1>mini2 and mini1>mini3):
    menor = mini1
elif (mini2>mini1 and mini2>mini3):
    menor = mini2
elif (mini3>mini2 and mini3>mini1):
    menor = mini3

print(f'Calc9 = {(maxi1 + maxi2 + maxi3)/menor}')

# 1.10) Pegue o maior valor de todas as listas e some com o menor valor de todas as listas

if (maxi1>maxi2 and maxi1>maxi3):
    maior = maxi1
elif (maxi2>maxi1 and maxi2>maxi3):
    maior = maxi2
elif (maxi3>maxi2 and maxi3>maxi1):
    maior = maxi3

print(f'Calc10 = {maior+menor}')
print('='*70)