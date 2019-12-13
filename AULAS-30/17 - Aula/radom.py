from random import randint
compar = randint (1,10)

num = 0

while not num == compar:
    num = int(input('Digite um numero(1-10): '))
    if num > compar:
        print('DICA: O numero é menor')
    elif num < compar:
        print('DICA: O numero é maior')
    else:
        print('VOCÊ ACERTOU!')
        break

