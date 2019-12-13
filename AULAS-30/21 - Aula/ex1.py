# Aula 21 - 06-12-2019
# Como Tratar e Trabalhar Erros!!!

# 1 - Crie um arquivo que leia 2 números inteiros e imprima a soma, 
# multiplicação, divisão e subtração com uma f-string.

# 2 - Crie um while que pergunte se deseja continuar. Se digitar 's' o
# programa termina.


# controle = 'n'
# while controle != 's':
#     n1 = int(input('Digite um numero:'))
#     n2 = int(input('Digite outro numero:'))
#     print (f'Soma: {n1+n2}')
#     print (f'Divisão: {n1/n2}')
#     print (f'Multiplicação: {n1*n2}')
#     print (f'Subtração: {n1-n2}')
#     controle = input ("Digite 's' para sair: ")

##################
while True:
    try:  
        print('Passou 1')
        n1 = int(input('Digite um numero:'))
        n2 = int(input('Digite outro numero:'))
        print(n1/n2)
        print('Passou 2')
    
    except (ValueError, ZeroDivisionError):
        print('Numero invalido')
    
    # except ZeroDivisionError:
    #     print('Divisão por zero')
    
    else:
        print('FIM')
        break






#################### até aqui tudo bem! ##########################

# 3 - faça um tratamento de exceção para que ao digitar o valor que 
# não seja inteiro, ele avise o usuário para ele digitar denovo.
# 4 - Faça outro tratamento de exceção para evitar que divida um numero
# por zero.