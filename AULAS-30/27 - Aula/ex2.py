# Aula 21 - 16-12-2019
#Operadores in is ==

from geradorlista import lista_simples_int_str
from geradorlista import lista_simples_int
from geradorlista import lista_simples_str
from geradorlista import embaralhar


# A função embaralhar() irá criar listas aleátorias, copiar-las
# e embaralhar. Desta forma não se sabe se as listas são iguais ou
# se as listas são as mesmas. Como defult ela irá criar 3 listas
# diferentes com 30 itens, copiálas e embaralar randomicamente
# retornando uma lista com o dobro (6) de itens.
print('='*70)
#lista = embaralhar(2,10)

# a = lista[0]
# b = lista[1]
# c = lista[2]
# d = lista[3]

# print(a)
# print(b)
# print(c)
# print(d)

# Neste caso, ele irá criar 2 listas com 10 itens, e retornará
# uma lista com 4 listas podendo cada uma ser cópia ou uma só.

lista = embaralhar(2,10,2)
print(lista)
print('*'*50)
# 1) Analisnado a lista gerada (possui 2 listas), diga se as duas listas são elas
# mesmas (is) ou são somente iguais (==).
if lista[1] is lista[0] and lista[0] == lista[1]:
    print('mesma e igual')
elif lista[0] == lista[1]:
    print('igual')
else:
    print('nem a mesma, nem igual')
# 2) Qual é o maior valor destas duas listas 
a = 0
c = 0
for b in lista[0]:
    if b > a:
        a = b
for b in lista[1]:
    if b > c:
        c = b

if a > c:
    maior = a
else:
    maior = c
print(f'Maior das duas listas = {maior}')

# 3) Qual é o maior valor de cada lista
print(f'Maior valor lista[0] é {max(lista[0])}')
print(f'Maior valor lista[1] é {max(lista[1])}')

# 4) Há o número 10 dentroDda lista[0]
print(f'4- {10 in lista[0]}')

# 5) Há o número 20 dentro da lista[1]?
print(f'5- {20 in lista[1]}')

# 6) Quantos números da lista[0] tem dentro da lista[1]?
count = 0
for b in lista[0]:
    if b in lista[1]:
        count +=1
print(f'Existem {count} numeros da lista[0] na lista[1]')

# 7) Mostre os números da lista[0] que estão dentro da lista[1]
n = 0
for b in lista[0]:
    if b in lista[1]:
        print(f'{n}- {b}')
    n +=1
# 8) Mutliplique a soma da lista[0] com cada item da lista[1]
soma0 = sum(lista[0])
x = 0
print(f'Resultados das multiplicações:')
for b in lista[1]:
    res = b * soma0
    print(f'\t{x}- {res}')
    x +=1
# 9) Faça uma divizão inteira do maior número da lista pelo menor numero da lista. Após verifique 
# se o resultado está dentro de uma das listas, se sim, diga qual!
j = 1000000
k = 1000000
for h in lista[0]:
    if h <= j:
        j = h
for h in lista[1]:
    if h <= k:
        k = h

if j < k:
    menor = j
else:
    menor = k

calc = maior // menor
print(f'RES DA DIV: {calc}')
print('Exercicio 9')

for b in lista[0]:
    if b == calc:
        print(f'Na lista[0]- {b}')
   
for b in lista[1]:
    if b == calc:
        print(f'Na lista[1]- {b}')


# 10) Verifique se o maior número da lista[0] está dentro da lista[1] e se o menor número da
# lista[1] está na lista[0]
print(f'maior0 {a}')
print(f'menor1 {k}')
for b in lista[1]:
    if a == b:
        print('O maior numero da lista[0] esta contido na lista[1]')
for b in lista[0]:
    if k == b:
        print('O menor numero da lista[1] esta contido na lista[0]')

print('='*70)