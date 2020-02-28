'''
Um espaço binário dentro de um número inteiro positivo N é qualquer sequência máxima de zeros consecutivos
que está rodeado por 1 dos dois lados na representação binária de N.

Por exemplo, o número 9 tem representação binária 1001 e contém uma lacuna binária de comprimento 2.
O número 529 tem representação binária 1000010001 e contém duas lacunas binárias:
um de comprimento 4 e um de comprimento 3.
O número 20 tem representação binária 10100 e contém um espaço binário de comprimento 1.
O número 15 tem representação binária 1111 e não possui lacunas binárias.
O número 32 tem representação binária 100000 e não possui lacunas binárias.

Escreva uma função:

solução def (N)

que, dado um número inteiro positivo N, retorna o comprimento de seu maior intervalo binário.
A função deve retornar 0 se N não contiver um espaço binário.

Exemplo, dado N = 1041, a função deve retornar 5,
porque N tem representação binária 10000010001 e, portanto, seu maior intervalo binário tem o comprimento 5.

Dado N = 32, a função deve retornar 0, porque N tem representação binária '100000'
e, portanto, sem lacunas binárias.
'''

# class Binario:
#     def __init__(self, n):
#         self.n = n
#
#     def contar(self):
#         num = bin(self.n)
#         lista_num = []

# passador=False
# def convert_to_binary(natural_number):
#
#     natural_number_to_binary = bin(natural_number)
#     x_binary = natural_number_to_binary[2:]
#     return x_binary
#
# def count_binary_space(binary):
#     list=[]
#     for i in binary:
#         list.append(i)
#
#     print(list)
#     x=(len(list)-1)
#
#     for i in range(1,x):
#         if '1' in list[i]:
#             passador=True
#
#
#     if passador==False and "1" in list[0] and '1' not in list[x]:
#         print("aarafafa")
#         return 0
#
#     list_with_zeros = binary.split('1') #splited '1', now we have a list with only zeros
#     max_zero_in_list = len(max(list_with_zeros))
#     message = f'o maior intervalo binário de {binary} é {max_zero_in_list}'
#     return print(message)
#
# x = convert_to_binary(32)
# count_binary_space(x)


def solution(N):
    n_bin = bin(N)[2:]
    result = n_bin.strip('0').strip('1').split('1')
    return len(max(result))

print(solution(15))